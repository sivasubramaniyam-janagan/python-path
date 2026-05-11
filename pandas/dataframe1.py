import pandas as pd
data={
            "name":["janagan","rukshi","talion","geralt"],
            "age":[23,24,35,70]
    }

df=pd.DataFrame(data,index=range(1,5))
print(df)
new_row=pd.DataFrame([{"name":"edward","age":28}],index=["new"])
df=pd.concat([df,new_row])
print(df)
