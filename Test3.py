import pandas as pd

res = pd.read_excel("Campus_Placement.xlsx")
print(res)

print("\n--Last 5 Records from Excel sheet--\n")
print(res.head())