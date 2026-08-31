class Solution:
    def reverseNumber(self, n):
        num=n
        res=0
        while num>0:
            temp=num%10
            res=res*10+temp
            num=num//10
        return res