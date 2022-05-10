#HANDLING MISSING VALUES
import pandas as pd
df=pd.read_csv('salaries.csv')
print(df.head())
df["service"].fillna(df['service'].mean(),inplace=True) #replace with average
print(df)