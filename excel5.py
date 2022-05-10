#HANDLING MISSING VALUES
import pandas as pd
df=pd.read_csv('salaries.csv')
print(df.head())
print(df.dropna())  #not to print row where any element is null