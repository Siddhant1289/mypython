import pandas as pd
st={'ROLLNO':[1,2,3,4],'NAME':['ABHAY','ANKIT','AMAN','SIDDHANT'],'MARKS':[70,68,73,75]}
df=pd.DataFrame(st,index=['r0','r1','r2','r3'])  #key and value type
print(df)
print(df['MARKS'])  # perticular