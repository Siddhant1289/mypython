import pandas as pd
df=pd.read_csv('salaries.csv')
print(df[0:1])  #index
print('')
print(df[0:3])  #slice
print('')
print(df.iloc[0:2,0:4])  #row and column
print('')
print(df[df.sex=='Male'])   #using criteria