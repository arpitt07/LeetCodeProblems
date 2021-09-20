class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # conver it to int first to do the sum and then convert it back to binary
        c = bin(int(a, 2) + int(b, 2))
        return (c[2:])
