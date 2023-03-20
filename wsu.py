import pandas as pd
from pathlib import Path
from openpyxl import load_workbook
file_name=Path('/mnt/c/Users/tbaur/Downloads/Birthday 2023 Triggers and Lists.xlsx')
all_sheets=pd.read_excel(file_name,sheet_name=None,engine='openpyxl')
df=pd.DataFrame()
for sheet in all_sheets:
    if sheet=="Triggers":
        continue
    all_sheets[sheet]['List']=sheet
    df=pd.concat([df,all_sheets[sheet]])

#writer=pd.ExcelWriter(file_name)
#if file_name.exists():
#    book=load_workbook(file_name,read_only=True)
 #   writer.book=book

#df.to_excel(writer,sheet_name='Combined',index=False)
#writer.close()
df.to_csv(file_name.parent / "Combined.csv", index=False)

