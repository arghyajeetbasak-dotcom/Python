from functools import reduce
l1=[34,21,96,75,58,101]
l2=[4,169,676]
sqRoot=lambda x:x**0.5
root=list(map(sqRoot,l2))
print(root)
def even(n):
    if(n%2==0):
        return True
    return False
OnlyEven=filter(even,l1)
print(list(OnlyEven))
def greatest(a,b):
    if(a>b):
        return a
    return b
result=reduce(greatest,l1)
print(result)