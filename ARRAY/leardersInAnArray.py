class Solution:
    def leaders(self, arr):
        # code here
        n=len(arr)
        res=[]
        res.append(arr[-1])
        maxi=arr[-1]
        for i in range(n-2,-1,-1):
            if arr[i]>=maxi:
                res.append(arr[i])
                maxi=arr[i]
        res.reverse()
                
        return res