class Solution:
    def romanToInt(self, s: str) -> int:

        romandict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        value = 0
        prev = 0

        for i in s[::-1]:
            current = romandict[i]
            if prev > current:
                value -= romandict[i]
            else:
                value += romandict[i]

            prev = current

        return value

if __name__ == "__main__":
    d = Solution()
    print(d.romanToInt("III"))
