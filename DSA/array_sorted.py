arr=[3,6,8,9,10,20]
n=len(arr)
def sorted(arr):
    for i in range(0,n-1):
        if(arr[i]>arr[i+1]):
            return f"The array is not sorted"
    return f"The array is sorted"
print(sorted(arr))