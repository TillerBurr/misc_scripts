import pandas as pd
from pathlib import Path


def combine_all_files(dir: str):
    new_path = Path(dir)
    merged = pd.DataFrame(columns=["ID", "Filename"])
    for file_ in new_path.glob("*"):
        print(file_.stem)
        df = pd.read_csv(file_.as_posix(), header=None)
        df = df.iloc[:, [0]]

        df.columns = ["ID"]
        df["Filename"] = file_.stem
        pd.concat([merged, df])

    merged.to_csv(new_path / "merged.csv", index=False)


if __name__ == "__main__":
    combine_all_files(".data/KU")
