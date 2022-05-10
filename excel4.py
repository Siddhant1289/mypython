#HANDLING MISSING VALUES
import pandas as pd
df=pd.read_csv('salaries.csv')
print(df.head())
df["service"].fillna('no value',inplace=True)
print(df)