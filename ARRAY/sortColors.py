# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         c1=0
#         c2=0
#         c3=0
#         for num in nums:
#             if num==0:
#                 c1+=1
#             elif num==1:
#                 c2+=1
#             else:
#                 c3+=1

#         for i in range(0,c1):
#             nums[i]=0
#         for j in range(c1,c1+c2):
#             nums[j]=1
#         for k in range(c1+c2,c1+c2+c3):
#             nums[k]=2


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        low=0
        mid=0
        high=n-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
