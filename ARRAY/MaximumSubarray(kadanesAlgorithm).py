from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        currSum=0
        maxSum=float("-inf")
        if n==1:
            return nums[0]

        for i in range(n):
            currSum+=nums[i]
            if currSum>maxSum:
                maxSum=currSum
            if currSum<0:
                maxSum=max(currSum,maxSum)
                currSum=0
        
        return maxSum