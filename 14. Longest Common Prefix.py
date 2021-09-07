from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minx = min(strs)
        maxx = max(strs)

        if not strs:
            return ""

        for i, j in enumerate(minx):
            if j != maxx[i]:
                return minx[:i]

        return minx


if __name__ == "__main__":
    d = Solution()
    print(d.longestCommonPrefix(["dog","doodle", "dodge"]))


#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".