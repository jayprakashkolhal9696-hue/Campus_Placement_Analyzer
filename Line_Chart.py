import pandas as pd
import matplotlib.pyplot as plt

# Load file
df = pd.read_excel("Campus_Placement.xlsx")
print(df)

# # Remove duplicate students
# df_clean = df.drop_duplicates(subset="Student_ID")

# # Filter placed students
# placed_students = df_clean[df_clean["Placement_Company"].notna() & 
#                             (df_clean["Placement_Company"] != "None")]

# # Group by Year
# yearly_placements = placed_students.groupby("Year")["Student_ID"].count()

# # Plot line chart
# plt.figure()
# plt.plot(yearly_placements.index, yearly_placements.values, marker="o")
# plt.title("Yearly Placement Trend")
# plt.xlabel("Year")
# plt.ylabel("Number of Placed Students")
# plt.show()
