# %%
import pathlib
import pandas as pd

p = pathlib.Path(__file__).parent
files = list(p.glob("*.csv"))
for file in files:
    dta = pd.read_csv(file, delimiter="|")
    dta.to_csv(file, index=False)
