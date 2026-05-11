import pandas as pd
data=pd.read_csv("data.csv",index_col="student_id")

print(data.loc["S012" : "S015",["name"]])
