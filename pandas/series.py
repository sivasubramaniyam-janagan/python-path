import pandas as pd

name=["Jana","rukshi","rockey","eren","light","yagami"]
marks=[99,90,78,75,80,76]

series=pd.Series(marks,index=name)
print(series)
series.loc["Jana"]=100
print(series.iloc[0])

print(series[series>=80] )
