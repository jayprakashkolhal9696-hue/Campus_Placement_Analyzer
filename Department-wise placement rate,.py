import pandas as pd
df=pd.read_excel("Campus_Placement.xlsx") 
df_clean = df.drop_duplicates(subset="Student_ID")

# dept_total = df_clean.groupby("Department")["Student_ID"].count()
# dept_placed = df_clean[df_clean["Placement_Company"] != "None"] \
#                 .groupby("Department")["Student_ID"].count()
# dept_placement_rate = (dept_placed / dept_total) * 100
# print(dept_placement_rate)

print(df_clean)
