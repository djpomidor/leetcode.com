# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        for j in range(len(strs[i])):
            if strs[0][j] == strs[i+1][j]:
                prefix = prefix + strs[i][j]
                i = i+1
                if i >= len(strs) - 1:
                    i = 1
            else:
                return prefix
        return prefix

    

strs = ["flower","flowffff","loght"]
s = Solution()
print(s.longestCommonPrefix(strs))
