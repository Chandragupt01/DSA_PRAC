class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        sum_map=dict()
        total=0
        maxlen=0
        n=len(arr)
        for i in range(0,n):
            total+=arr[i]
            if total==k:
                maxlen=i+1
            
            rem=total-k
            if rem in sum_map:
                l=i-sum_map[rem]
                maxlen=max(l,maxlen)
                
            if total not in sum_map:
                sum_map[total]=i
        return maxlen
