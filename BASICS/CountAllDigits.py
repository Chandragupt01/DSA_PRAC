class Solution:
    def countDigit(self, n):
        res = 0
        num = n
        while num > 0:
            num = num//10
            res += 1
        return res
