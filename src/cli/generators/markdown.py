from pathlib import Path
from generators.honeytoken import HoneyTokenGenerator
import shutil

class MarkdownGenerator(HoneyTokenGenerator):
    def generate(self, output_path: str, endpoint_base_uri: str, **kwargs):
        if 'input_path' not in kwargs:
            print('No input file provided')

        input_path = Path(kwargs['input_path'])
        if not input_path.exists():
            print("File not found")
            return

        out = Path(output_path)

        shutil.copy(input_path, out)

        with out.open("a", encoding="utf-8") as f:
            f.write(f"\n\n![status]({endpoint_base_uri}.png)\n")
        print(f"Wrote {out}")
