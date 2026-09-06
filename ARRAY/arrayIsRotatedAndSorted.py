from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        rotation=0
        for i in range(1,n):
            if nums[i-1]<=nums[i]:
                continue
            else:
                rotation+=1
        return (rotation==1 and nums[0]>=nums[n-1]) or rotation==0 

# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         rotation=0
#         n=len(nums)
#         for i in range(len(nums)):
#             if nums[i]>nums[(i+1)%n]:
#                 rotation+=1
#             if rotation >1:
#                 return False
#         return True
