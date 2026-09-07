from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        n=len(nums)
        for i in range(n):
            freq[nums[i]]=freq.get(nums[i],0)+1
        
        for k,v in freq.items():
            if v==1:
                return k
        return -1