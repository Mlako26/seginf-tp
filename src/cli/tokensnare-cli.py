import click
import requests
import tomllib

from generators.mysql_dump import MysqlDumpGenerator
from generators.markdown import MarkdownGenerator
from generators.honeytoken import HoneyTokenGenerator
from generators.binary import BinaryHoneyTokenGenerator
from generators.email import EmailHoneyTokenGenerator
from generators.qr import QRHoneyTokenGenerator


def generate_token(type: str, output_path: str, **kwargs) -> None:
    endpoint_base_url = get_endpoint_base_uri()
    token_generator = get_token_generator(type)
    token_generator.generate(output_path, endpoint_base_url, **kwargs)


def get_endpoint_base_uri() -> str:
    with open("config.toml", "rb") as f:
        cfg = tomllib.load(f)

    try:
        return requests.get(
            f"http://{cfg['webserver']['host']}:{cfg['webserver']['port']}/new",
            timeout=5
        ).json().get("url")
    except Exception:
        print(f"Failed connecting to the web-server at {cfg['webserver']['host']}:{cfg['webserver']['port']}")
        quit(1)


def get_token_generator(type: str) -> HoneyTokenGenerator:
    with open("config.toml", "rb") as f:
        cfg = tomllib.load(f)

    match type:
        case "markdown":
            return MarkdownGenerator()
        case "mysql-dump":
            return MysqlDumpGenerator(cfg['mysql_dump']['default_dump_path'])
        case "binary":
            return BinaryHoneyTokenGenerator()
        case "email":
            return EmailHoneyTokenGenerator()
        case "qr":
            return QRHoneyTokenGenerator()
        case _:
            print("No generator defined for this type of HoneyToken")
            quit(1)


@click.group()
def tokensnare():
    """
    === .: TokenSnare-CLI :. ===
    
    Tool that handles the generation and subscription of HoneyTokens
    """


@tokensnare.command("markdown")
@click.option("--input", "-i", help="Markdown input file to transform into a HoneyToken", required=True)
@click.option("--output", "-o", help="File path were the token will be created at", required=True)
def generate_markdown(input: str, output: str) -> None:
    generate_token("markdown", output,  input_path=input)


@tokensnare.command("qr")
@click.option("--output", "-o", help="File path were the token will be created at", required=True)
def generate_qr(output: str):
    generate_token("qr", output)


@tokensnare.command("binary")
@click.option("--output", "-o", help="File path were the token will be created at", required=True)
def generate_binary(output: str):
    generate_token("binary", output)



@tokensnare.command("mysql-dump")
@click.option("--output", "-o", help="File path were the token will be created at", required=True)
@click.option("--input", "-i", help="Dump file to be tokenized. If not provided a generic dump will be generated")
def generate_mysql_dump(output: str, input: str | None) -> None:
    generate_token("mysql-dump", output, input_path=input)


@tokensnare.command("web-page")
@click.option("--output", "-o", help="File path were the token will be created at", required=True)
def generate_web_page(output: str):
    print("web-page generated!")


@tokensnare.command("email")
@click.option("--output", "-o", help="File path were the token will be created at", required=True)
def generate_email(output: str):
    generate_token("email", output)


if __name__ == '__main__':
    tokensnare()
