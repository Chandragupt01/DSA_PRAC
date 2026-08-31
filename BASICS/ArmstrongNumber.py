class Solution:
    def isArmstrong(self, n):
        p=len(str(n))
        num=n
        res=0
        while(num>0):
            digi=num%10
            res+=digi**p
            num=num//10

        return n==res