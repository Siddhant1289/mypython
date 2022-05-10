import pandas as pd
import numpy as np
da=np.array(['a','b','c','d'])
s=pd.Series(da,index=[701,702,703,704])  #index no.
dt={'a':501,'b':505,'c':508}
s1=pd.Series(dt,index=['c','a','b'])
print(s)
print(s1)