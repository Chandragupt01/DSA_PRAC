class Solution:
    def mostFrequentElement(self, nums):
        freq={}
        max_freq=0
        max_el=float('inf')
        for num in nums:
            freq[num]=freq.get(num,0)+1
            count=freq[num]

            if count>max_freq or (count==max_freq and num<max_el):
                max_freq=count
                max_el=num

        return max_el