import pandas as pd

res = pd.read_excel("Campus_Placement.xlsx")
print(res)

print(res.isnull().sum())