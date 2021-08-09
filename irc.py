from pathlib import Path
import pandas as pd
from datetime import datetime
from icecream import ic


def append_booster_data(path: Path):
    df = pd.DataFrame()
    for _file in path.glob("*.xls"):
        data = pd.read_excel(_file, engine="xlrd")

        date = _file.stem.replace("all play ", "")
        date = datetime.strptime(date, "%m-%d-%Y")
        data["Play Date"] = date
        df = pd.concat([df, data])
    df = df.dropna(subset=["PlayerLevel"])
    return df


if __name__ == "__main__":
    file_path = Path(".data/")
    df = append_booster_data(file_path)
    df.to_csv(".data/Combined.csv")
