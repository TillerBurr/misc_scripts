import pandas as pd
from pathlib import Path
combined=pd.DataFrame()
for file_ in Path('.data/wrrc').glob('*.xlsx'):
    print(file_)
    df = pd.read_excel(file_)
    combined=pd.concat([combined,df])

combined.to_csv('.data/combined.csv')
