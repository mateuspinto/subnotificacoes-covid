import os
from pathlib import Path

WORK_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parents[1]
RAW_DATA_DIR = WORK_DIR / 'data' / 'raw'
PROCESSED_DATA_DIR = WORK_DIR / 'data' / 'processed'

if __name__ == "__main__":
    print(f'WORK_DIR={WORK_DIR}')
    print(f'RAW_DATA_DIR={RAW_DATA_DIR}')
    print(f'PROCESSED_DATA_DIR={PROCESSED_DATA_DIR}')