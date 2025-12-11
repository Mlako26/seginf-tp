from pathlib import Path
import shutil
from generators.honeytoken import HoneyTokenGenerator

class MysqlDumpGenerator(HoneyTokenGenerator):
    def __init__(self, default_dump_path: str) -> None:
        super().__init__()
        self.default_dump_path = default_dump_path
    
    def generate(self, output_path: str, endpoint_base_uri: str, **kwargs):
        output = Path(output_path)
        
        if kwargs['input_path'] is None:
            input = Path(self.default_dump_path)
        else:
            input = Path(kwargs['input_path'])
            
        shutil.copy(input, output)
        
        with output.open("a", encoding="utf-8") as f:
            f.write("\n")
            f.write("STOP REPLICA;\n")
            f.write(f"CHANGE MASTER TO MASTER_HOST='{endpoint_base_uri}', MASTER_PORT=3306, MASTER_USER='root', MASTER_PASSWORD='root', MASTER_RETRY_COUNT=1;\n")
            f.write(f"START REPLICA;\n")
        print(f"Mysql dump token generated at {output}")
