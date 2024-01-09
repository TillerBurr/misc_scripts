import pandas as pd
from pathlib import Path

gl=Path("/mnt/x/Association & Membership/NC Sheriffs Assc/Mailings/Fall Prospecting/Rented Lists")
def combine(dir:Path):
    df=pd.DataFrame()
    for fpath in dir.glob("*.csv"):
        print(fpath.name)
        temp=pd.read_csv(fpath)
        df=pd.concat([df,temp])

    df.to_csv(gl / 'combined.csv')


if __name__=="__main__":
    combine(gl)
