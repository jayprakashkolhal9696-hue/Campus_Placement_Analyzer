import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("Campus_Placement.xlsx")  


df_clean = df.drop_duplicates(subset="Student_ID")

dept_placed = df_clean[df_clean["Placement_Company"] != "None"] \
                .groupby("Department")["Student_ID"].count()

plt.figure()
dept_placed.plot(kind="bar")
plt.title("Department-wise Placements")
plt.xlabel("Department")
plt.ylabel("Number of Placed Students")
plt.xticks(rotation=45)
plt.show()

