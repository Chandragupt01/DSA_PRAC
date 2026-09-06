from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=i+1
        while j<n:
            if nums[i]==nums[j]:
                j=j+1
            else:
                nums[i+1],nums[j]=nums[j],nums[i+1]
                i+=1
                j+=1
        return i+1