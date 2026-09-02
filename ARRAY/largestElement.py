class Solution:
    def largestElement(self, nums):
        largest=float('-inf')
        for i in nums:
            if i>largest:
                largest=i
        
        return largest