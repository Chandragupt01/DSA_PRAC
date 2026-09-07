from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                maxi=max(count,maxi)
                count=0
        return max(count,maxi)