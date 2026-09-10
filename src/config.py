from dataclasses import dataclass
from pathlib import Path

@dataclass
class ReportConfig:
    input_file: Path
    output_dir: Path