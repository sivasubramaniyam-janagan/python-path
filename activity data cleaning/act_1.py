import pandas as pd

details=pd.read_csv("data.csv")
print(details.head())

print("-----------------------------------------------------------------------------------------------------")

print(details.info())

print("-----------------------------------------------------------------------------------------------------")

print(details.describe())

print("-----------------------------------------------------------------------------------------------------")

details["name"]=details.name.str.replace(" ","")
details["department"]=details.department.str.title()

print(details)

print("-----------------------------------------------------------------------------------------------------")

print(details.isnull().sum())

#median_age=details.age.median()
mean_gpa=details.gpa.mean()
details.gpa=details.gpa.fillna(mean_gpa)

details.gender=details.gender.fillna("Unknown")
print(details.head())

details.attendance=pd.to_numeric(details.attendance.str.replace("%",""))



