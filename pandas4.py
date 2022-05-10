import pandas as pd
s=pd.Series([2,5,7,8],index=['a','b','c','d'])
print(s)
print(s[1])
print(s[:3])
print(s[-3:])
#print(s['e'])  #key error