#FILLER DATA ON CONDITIONS
import pandas as pd
df=pd.read_csv("salaries.csv")
df=df[df['salary']>90000]
print(df)
#we can use & and | for multiple condition
df=df[(df['salary']>90000)&(df['sex']=='Male')]
print(df)