from pathlib import Path
from generators.honeytoken import HoneyTokenGenerator

EMAIL_TEMPLATE = """From: "Soporte" <soporte@example.com>
To: destinatario@example.com
Subject: Informe Confidencial

MIME-Version: 1.0
Content-Type: text/html; charset="utf-8"

<html>
  <body>
    <p>Hola,</p>
    <p>Este es un mensaje confidencial. Por favor, no lo compartas.</p>

    <!-- Tracking pixel del honeytoken -->
    <img src="{tracking_url}.png" alt="" style="display:none" />
  </body>
</html>
"""

class EmailHoneyTokenGenerator(HoneyTokenGenerator):
    def generate(self, output_path: str, endpoint_base_uri: str, **kwargs):
        out = Path(output_path)
        content = EMAIL_TEMPLATE.format(tracking_url=endpoint_base_uri)
        out.write_text(content, encoding="utf-8")
        print(f"Email honeytoken generated at: {out}")
