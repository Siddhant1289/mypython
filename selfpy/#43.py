

nums=[3,2,4,5,6,8,7,9]

evens=list(filter(lambda n: n%2==0,nums))

double=list(map(lambda n: n*2,nums))

print(evens)
print(double)