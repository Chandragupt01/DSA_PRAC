# class Solution:
#     def missingNumber(self, nums):
#         n=len(nums)
#         for i in range(n+1):
#             if i not in nums:
#                 return i

def missingNumber(nums):
    arrsum=sum(nums)
    n=len(nums)
    total=((n*(n+1))//2)
    return int(total-arrsum)

print(missingNumber([0,2,3,1,4]))