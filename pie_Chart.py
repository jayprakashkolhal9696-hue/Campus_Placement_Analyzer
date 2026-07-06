import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("Campus_Placement.xlsx")
df_clean = df.drop_duplicates(subset="Student_ID")  
company_counts = df_clean[df_clean["Placement_Company"] != "None"] \
                    ["Placement_Company"].value_counts()

plt.figure()
company_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Company-wise Student Distribution")
plt.ylabel("")
plt.show()
