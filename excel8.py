#import new column
import pandas as pd
df=pd.read_csv('salaries.csv')
df.insert(6,'test',df['service']+10)
print(df)