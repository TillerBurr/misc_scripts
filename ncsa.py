import pandas as pd
from pathlib import Path
from rich import print
from rich.prompt import Prompt

combined_df = pd.DataFrame()
df_counts = pd.DataFrame(columns=["File", "Count"])
bad_headers = []
for _file in Path(".").glob("*.xlsx"):
    print(_file.name)
    df = pd.read_excel(_file)
    if df.columns.values != ["Email"]:
        bad_headers.append(_file.name)

    combined_df = pd.concat([combined_df, df])
    counts = pd.DataFrame([{"File": _file.name, "Count": len(df)}])
    df_counts = pd.concat([df_counts, counts])

if len(bad_headers) > 0:
    print("[red]The following files have a bad header:[/red]")
    print(bad_headers)
    print("[red]Please change the header to be 'Email' and run again[/red]")
    Prompt.ask("[red]Press Enter to continue[/red]")

else:
    combined_df.to_csv("./Combined Emails.csv", index=False)
    df_counts.to_csv("./Counts by File.csv", index=False)
    file_path = Path("./Combined Emails.csv").resolve()
    counts = Path("./Counts by File.csv").resolve()

    print("[green]You can find the output at:[/green]")
    print(f"[green]{file_path} and {counts}[/green]")
    Prompt.ask("[green]Press Enter to continue:[/green]")
