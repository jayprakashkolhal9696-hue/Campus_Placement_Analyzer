import pandas as pd

# Load dataset
df = pd.read_excel("Campus_Placement.xlsx")  
# print(df)



df["Name"] = df["Name"].str.title()
df["Gender"] = df["Gender"].str.upper()
df["Department"] = df["Department"].str.title()
df["Course"] = df["Course"].str.title()
df["Placement_Company"] = df["Placement_Company"].str.title()
df["Role"] = df["Role"].str.title()
df["PIP_Status"] = df["PIP_Status"].str.upper()

print(df.head())



# Example of title(): 
#title():It is used to every new string first letter is alphabet
# Before: "bhushan musale".title()
#After apply title():Bhushan Musale  


#Upper():

#Function	       What It Does                                Example  Input	               Output
# .upper()	     All letters capital 	                           "hello"	                    HELLO
#.title()        First letter capital                          "hello world"                 Hello World