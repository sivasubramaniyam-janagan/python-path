import pandas as pd

stu_marks={"jana":100,"rukshi":90,"light":80}

series=pd.Series(stu_marks)
print(series)

eligible=series[series>=90]
print(eligible)

print(series.iloc[0])
