import pandas as pd

data=pd.read_csv("data.csv")
print(data) #to print all

#selection
print(data[["gpa","name"]])
