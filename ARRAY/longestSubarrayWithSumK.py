# class Solution:
#     def longestSubarray(self, arr, k):  
#         # code here
#         n=len(arr)
#         maxi=0
#         for i in range(n):
#             sum=0
#             for j in range(i,n):
#                 sum+=arr[j]
#                 if sum==k:
#                     maxi=max(maxi,j-i+1)
#         return maxi

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        n=len(arr)
        maxi=0
        l,r=0,0
        sum=arr[0]
        while r<n:
            while l<=r and sum>k:
                sum=sum-arr[l]
                l+=1
                
            if sum==k:
                maxi=max(maxi,r-l+1)
            r+=1
            if r<n:
                sum+=arr[r]
        return maxi
            
    
