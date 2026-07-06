import pandas as pd

df = pd.read_excel("Campus_Placement.xlsx")
print(df)

df["Salary"] = df.groupby("Placement_Company")["Salary"].transform(
    lambda x: x.fillna(x.mean())
)