import numpy as np
a='hello'
e=np.char.center(a,50,'*')
print(e)
print(np.char.title(a))
print(np.char.upper(a))
print(np.char.lower(a))
print(np.char.capitalize(a))



s="THIS IS PYTHON"
print(np.char.split(s))       #   o/p=['THIS', 'IS', 'PYTHON']


print(np.char.join(':',s))    #   o/p=T:H:I:S: :I:S: :P:Y:T:H:O:N