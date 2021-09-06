class Solution:
    def isPalindrome(self, x: int) -> bool:
        # use slice notation and reverse the input, if it matches with original, then its a palindrome
        y = abs(x)
        minx = -2 ** 31
        maxx = 2 ** 31 - 1

        tempstr = str(y)

        output = int(tempstr[::-1])

        if x in range(minx, maxx):
            if x == output:
                return True
            else:
                return False

if __name__ == "__main__":
    d = Solution()
    print(d.isPalindrome(123))

#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.