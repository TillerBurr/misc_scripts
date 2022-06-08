from pathlib import Path
import pandas as pd
from datetime import datetime
from icecream import ic


def append_booster_data(path: Path):
    df = pd.DataFrame()

    for _file in path.glob("*.csv"):
        try:
            data = pd.read_csv(_file)
        except UnicodeDecodeError:
            data = pd.read_csv(_file,encoding='cp1252')
        data['file_name'] = _file.stem
        data['Washington']=data['State'].apply(lambda x: "WA" if x=="WA" else "Not WA")

        df = pd.concat([df, data])
    return df


if __name__ == "__main__":
    base_dir=".data/uwaa acq"
    file_path = Path(
        base_dir
    )
    df = append_booster_data(file_path)
    counts = df['Washington'].reset_index().groupby('Washington').count()
    counts['Percent of Total'] = counts['index']/counts['index'].sum()
    counts = counts.rename(columns={'index':'Count'})
    counts.to_csv(file_path / "Washington_counts.csv")
    df.to_csv(file_path / "Combined.csv")
