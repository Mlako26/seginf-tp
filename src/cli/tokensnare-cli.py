import click
import requests

from tokens.markdown import MarkdownGenerator
from tokens.honeytoken import HoneyTokenGenerator

def get_endpoint_base_uri():
    token_id = requests.get("http://127.0.0.1:8080/new").json().get("id")
    ip = requests.get("https://api.ipify.org").text
    return f"http://{ip}:8080/resource/{token_id}"

def get_token_generator(type: str) -> HoneyTokenGenerator:
    match type:
        case "markdown":
            return MarkdownGenerator()
        case _:
            print("No generator defined for this type of HoneyToken")
            quit(1)

@click.group()
def tokensnare():
    """
    === .: TokenSnare-CLI :. ===
    
    Tool that handles the generation and subscription of HoneyTokens
    """
    pass

@tokensnare.command("markdown")
@click.option("--input", "-i", help="Markdown input file to transform into a HoneyToken", required=True)
@click.option("--output", "-o", help="File path were the token will be created at", required=True)
def generate_markdown(input: str, output: str):
    endpoint_base_url = get_endpoint_base_uri()
    token_generator = get_token_generator("markdown")
    token_generator.generate(output, endpoint_base_url, input_path=input)

@tokensnare.command("qr")
@click.option("--output", "-o", help="File path were the token will be created at", required=True)
def generate_qr(output: str):
    print("qr generated!")
    
@tokensnare.command("binary")
@click.option("--output", "-o", help="File path were the token will be created at", required=True)
def generate_binary(output: str):
    print("binary generated!")
    
@tokensnare.command("mysql-dump")
@click.option("--output", "-o", help="File path were the token will be created at", required=True)
def generate_mysql_dump(output: str):
    print("mysql-dump generated!")

@tokensnare.command("web-page")
@click.option("--output", "-o", help="File path were the token will be created at", required=True)
def generate_web_page(output: str):
    print("web-page generated!")

@tokensnare.command("email")
@click.option("--output", "-o", help="File path were the token will be created at", required=True)
def generate_email(output: str):
    print("email generated!")

if __name__ == '__main__':
    tokensnare()
