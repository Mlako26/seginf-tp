from pathlib import Path
from generators.honeytoken import HoneyTokenGenerator
import stat

BINARY_SCRIPT_TEMPLATE = """
#!/usr/bin/env python3
import urllib.request

def main():
    url = {url!r}
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            resp.read(1)
    except Exception:
        # No nos importa si falla, solo queremos intentar reportar
        pass

if __name__ == "__main__":
    main()
"""

class BinaryHoneyTokenGenerator(HoneyTokenGenerator):
    def generate(self, output_path: str, endpoint_base_uri: str, **kwargs):
        out = Path(output_path)
        out.write_text(BINARY_SCRIPT_TEMPLATE.format(
            url=endpoint_base_uri), encoding='utf-8')
        
        # Make the script executable
        mode = out.stat().st_mode
        out.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)   
        print(f"Binary honeytoken script generated at: {out}")    