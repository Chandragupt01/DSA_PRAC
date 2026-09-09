from typing import List


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n=len(nums)
#         freq={}
#         for k in nums:
#             freq[k]=freq.get(k,0)+1
#         for k, v in freq.items():
#             if v>n//2:
#                 return k

## Boyer Moores voting algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        candidate=None
        for num in nums:
            if count==0:
                candidate=num
                count+=1

            elif num==candidate:
                count+=1
            else:
                count-=1
        return candidate
        