from pathlib import Path
from generators.honeytoken import HoneyTokenGenerator
import requests


class WebPageGenerator(HoneyTokenGenerator):
    def generate(self, output_path: str, endpoint_base_uri: str, **kwargs):
        url = kwargs.get("url")
        if not url:
            print("No URL provided")
            return

        try:
            html = requests.get(url, timeout=10).text
        except Exception as e:
            print(f"Fetch failed: {e}")
            return

        # Very simple GET-only beacon
        beacon = (
            "<script>\n"
            f"new Image().src = '{endpoint_base_uri}';\n"
            "</script>\n"
        )

        lower = html.lower()
        if "</body>" in lower:
            pos = html.rfind("</body>")
        else:
            pos = len(html)

        modified = html[:pos] + beacon + html[pos:]

        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(modified, encoding="utf-8")
        print(f"Wrote {out}")
