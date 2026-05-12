import pandas as pd
df=pd.read_csv("data.csv" , index_col="student_id")
mean=df.mean(numeric_only=True)
#print (mean)
sums=df["gpa"].sum()
#print(sums)

#print(df[df["gpa"]==df["gpa"].max() ])

group=df.groupby("year")
#print(group["year"].count())

df=df.drop(columns=["gpa"])
print(df)
