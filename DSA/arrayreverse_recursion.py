num=[5,7,3,2,6,1,4,9]
def revarray(arr,left,right):
    if left>=right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    revarray(arr,left+1,right-1)
revarray(num,0,7)
print(num)