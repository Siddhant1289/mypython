#MERGE DATASHEET
import pandas as pd
df=pd.read_csv('Emp.csv')
df1=pd.read_csv('EmpGrade.csv')
print(pd.merge(df,df1,on="Empno"))