import pandas as pd
dt=[[101,'ABC',21000],[102,'DEF',30000],[103,'GHI',35000]]
df=pd.DataFrame(dt,columns=['EMPNO','NAME','SALARY'])
print(df)