class Solution:    
    def palindromeCheck(self,s):
        #your code goes here
        def helper(left,right):
            if left>=right:
                return True
            if s[left]!=s[right]:
                return False
            return helper(left+1,right-1)
        return helper(0,len(s)-1)