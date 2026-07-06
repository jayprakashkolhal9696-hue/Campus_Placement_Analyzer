import pandas as pd
df=pd.read_excel("Campus_Placement.xlsx")  
print("CGPA Mean:",df["CGPA"].mean())
print("Technical_Skills Mean:",df["Technical_Skills"].mean())
print("Soft_Skills Mean:",df["Soft_Skills"].mean())
print("Training_Hours Mean:",df["Training_Hours"].mean())
print("Salary Mean:",df["Salary"].mean())
