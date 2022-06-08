from pathlib import Path
import pandas as pd
from datetime import datetime
from icecream import ic


def append_booster_data(path: Path):
    df = pd.DataFrame()
    for _file in path.glob("*.xlsx"):
        data = pd.read_excel(_file, engine="openpyxl")

        df = pd.concat([df, data])
    for _file in path.glob("*.csv"):
        data = pd.read_csv(_file,encoding='cp1252')

        df = pd.concat([df, data])
    return df


if __name__ == "__main__":
    base_dir=".data/mpm/merge"
    file_path = Path(
        base_dir
    )
    df = append_booster_data(file_path)
    df.to_csv(file_path / "Combined.csv")
