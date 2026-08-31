class Solution:
    def divisors(self, n):
        res=[]
        num=n
        for i in range(1,num+1):
            if n%i==0:
                res.append(i)

        return res