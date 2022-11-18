import pandas as pd

def combine_all():
    pth='.data/wsu/PCs.xlsx'
    dfs=pd.read_excel(pth,sheet_name=None)
    combined_df=pd.DataFrame()
    for sheet in dfs.keys():
        new_df=dfs[sheet]
        new_df['List']=sheet
        combined_df=pd.concat([combined_df,new_df])

    combined_df.to_csv('.data/wsu/combined_pcs.csv')


if __name__=="__main__":
    combine_all()