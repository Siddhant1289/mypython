#SORT DATABASE
import pandas as pd
df=pd.read_csv('salaries.csv')
print(df.sort_values("service",ascending=True)) #automatically sort in ascending order without TRUE
print('')
print(df.sort_values("service",ascending=False))