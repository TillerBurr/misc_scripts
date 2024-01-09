import pandas as pd
from pathlib import Path
from rich import print
from rich.prompt import Prompt

combined_df = pd.DataFrame()
bad_headers = []
for _file in Path(".data/ccmke").glob("*.xlsx"):
    print(_file.name)
    df = pd.read_excel(_file)
    combined_df = pd.concat([combined_df, df])

combined_df.to_csv("./Combined Emails.csv", index=False)
file_path = Path("./Combined Emails.csv").resolve()
counts = Path("./Counts by File.csv").resolve()

print("[green]You can find the output at:[/green]")
print(f"[green]{file_path}[/green]")
Prompt.ask("[green]Press Enter to continue:[/green]")
