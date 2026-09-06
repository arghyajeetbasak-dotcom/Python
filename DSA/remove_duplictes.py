class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        j=i+1
        while(j<len(nums)):
            if(nums[j]!=nums[i]):
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1
arr=[0,0,1,1,1,2,2,3,3,4]
a=Solution()
print(a.removeDuplicates(arr))