from pathlib import Path
import qrcode
from generators.honeytoken import HoneyTokenGenerator

class QRHoneyTokenGenerator(HoneyTokenGenerator):
    def generate(self, output_path: str, endpoint_base_uri: str, **kwargs):
        out = Path(output_path)

        # Generar QR con la URL completa del honeytoken
        img = qrcode.make(endpoint_base_uri)

        # Guardar como PNG
        img.save(out)

        print(f"QR honeytoken generated at: {out}")
