import pandas as pd
df=pd.read_csv("data.csv",index_col="student_id")
stu_id=input("Enter id to search")
try:
    
    print(df.loc[stu_id])
except KeyError as e:
    print("NOT FOUND")
