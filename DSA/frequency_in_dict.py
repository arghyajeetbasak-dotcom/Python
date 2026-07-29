nums=[5,6,7,7,1,1,8,111,5,1,1]
d={}
#  Method 1
for item in nums:
    if item in d:
        d[item]+=1
    else:
        d[item]=1
print(d)
#  Method 2
for item in nums:
    d[item]=d.get(item,0)+1
print(d)