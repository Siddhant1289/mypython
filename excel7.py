#HANDLING MISSING VALUES
import pandas as pd
df=pd.read_csv('salaries.csv')
print(df.head())
df["service"].fillna(df['service'].sum(),inplace=True) #replace with sum
print(df)