#drop duplicates according to column
import pandas as pd
df=pd.read_csv('salaries.csv')
print(df.drop_duplicates(subset='discipline'))