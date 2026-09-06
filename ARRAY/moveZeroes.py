from typing import List


def moveZeroes(nums: List[int]) -> None:
    i,j=0,0
    n=len(nums)
    while j<n:
        if nums[i]==0 and nums[j]==0:
            j+=1
        else:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         if len(nums) == 1:
#             return
#         i = 0
#         while i < len(nums):
#             if nums[i] == 0:
#                 break
#             i += 1
#         if i == len(nums):
#             return
#         j = i + 1
#         while j < len(nums):
#             if nums[j] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#             j += 1
arr=[0,1,0,3,12] 
moveZeroes(arr)
print(arr)
