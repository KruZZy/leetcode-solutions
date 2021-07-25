class Solution(object):
    def myPow(self, x, n):
        a = 1 
        if n < 0:
            x = 1/x 
            n *= -1 
        
        while n > 0:
            if n & 1:
                a *= x
            x *= x
            n >>= 1 
        return a 

S = Solution() 
print(S.myPow(10, 2))
