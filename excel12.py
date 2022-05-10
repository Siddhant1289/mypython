#APPEND DATASHEET
import pandas as pd
df=pd.read_csv("salaries.csv")
df1=pd.read_csv("salaries1.csv")
print(df.append(df1))