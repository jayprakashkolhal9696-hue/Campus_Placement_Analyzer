import pandas as pd
df=pd.read_excel("Campus_Placement.xlsx")  
total = df["Student_ID"].nunique()
placed = df[df["Placement_Company"] != "None"]["Student_ID"].nunique()
placement_percentage = (placed / total) * 100
print(placement_percentage,"%")






#Count how many unique students are in the dataset.
# Student_ID = student number
# nunique() = counts unique values (no duplicates)

#First, select only students who got placement
# (Placement_Company is NOT "None")
# Then count their unique Student_ID

#Divide placed students by total students
# Multiply by 100 to convert into percentage