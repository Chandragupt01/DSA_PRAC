# class Solution:    
#     def palindromeCheck(self,s):
#         #your code goes here
#         def helper(left,right):
#             if left>=right:
#                 return True
#             if s[left]!=s[right]:
#                 return False
#             return helper(left+1,right-1)
#         return helper(0,len(s)-1)

class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        res=""
        n=len(s)
        for i in range(n):
            if s[i].isalnum():
                res+=s[i].lower()
        start=0
        end=len(res)-1
        while start<end:
            if res[start]!=res[end]:
                return False
            start+=1
            end-=1
        return True