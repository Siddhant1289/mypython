#import CSV file
import pandas as pd
df=pd.read_csv("D:\\python\\Emp.csv")
print(df.head())   #start 5
print('')
print(df.head(2))  #start 2
print('')
print(df.tail())   #end 5
print('')
print(df.tail(2))  #end 2
print('')
print(df.dtypes)
print('')
print(df.shape)    #shape of data