n=int(input("Enter the number: "))
m=n
count=0
while(m!=0):
    digit=m%10
    count+=1
    m=m//10
print(count)
#     or
import math
result=math.log10(n)+1
print(int(result))