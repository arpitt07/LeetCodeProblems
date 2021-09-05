class Solution:
    def reverse(self, x: int) -> int:
        # turn the input in positive
        y = abs(x)
        minx = -2**31
        maxx = 2**31 - 1
        
        strn = str(y)
        
        if x > 0:
            rev = int(strn[::-1])
        if x <= 0:
            rev = -1 * int(strn[::-1])
            
        if minx > rev or maxx < rev:
            return 0
        else:
            return rev


#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the 
#signed 32-bit integer range [-231, 231 - 1], then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).