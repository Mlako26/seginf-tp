import sys
from pathlib import Path
import requests

def main():
    if len(sys.argv) < 2:
        print("Missing file path.")
        return

    path = Path(sys.argv[1])
    if not path.exists():
        print("File not found.")
        return

    md = path.read_text()

    r = requests.get("http://127.0.0.1:8080/new")
    token = r.json().get("id")

    ip = requests.get("https://api.ipify.org").text
    md += f"\n\n![status](http://{ip}:8080/resource/{token}.png)\n"

    out = path.with_name(path.stem + "_with_status.md")
    out.write_text(md)
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()


