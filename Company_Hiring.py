import pandas as pd
df=pd.read_excel("Campus_Placement.xlsx")  
# df[df["Placement_Company"] != "None"]["Placement_Company"].value_counts()
# total=df[df["Placement_Company"] != "None"]["Placement_Company"].value_counts()
total=df.drop_duplicates(subset="Student_ID") \
  .query("Placement_Company != 'None'")["Placement_Company"] \
  .value_counts()

print(total)