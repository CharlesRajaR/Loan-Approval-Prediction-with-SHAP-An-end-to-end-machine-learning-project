from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def load_accepted_loans_data(
    csv_name: str = "accepted_2007_to_2018Q4.csv.gz",
    data_dir: str | Path | None = None,
) -> pd.DataFrame:
    """Load the gzipped Lending Club loan dataset from the raw data folder."""
    base_dir = Path(data_dir) if data_dir is not None else RAW_DATA_DIR
    file_path = base_dir / csv_name

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    return pd.read_csv(file_path, compression="gzip")


if __name__ == "__main__":
    df = load_accepted_loans_data()
    print(df.head())
    print(f"Shape: {df.shape}")
