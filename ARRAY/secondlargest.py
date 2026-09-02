class Solution:
    def secondLargestElement(self, nums):
        largest=nums[0]
        secondLargestElement=float('-inf')
        if len(nums)<2:
            return -1

        for num in nums:
            if num>largest:
                secondLargestElement=largest
                largest=num
            elif num>secondLargestElement and num!=largest:
                secondLargestElement=num
        if secondLargestElement==float('-inf'):
            return -1
        return secondLargestElement