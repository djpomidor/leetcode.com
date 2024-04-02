# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        for x in strs[0]:
            if x != (strs[1][i] and strs[2][i]):
                break
            else:               
                prefix += x
                i+=1
        return prefix        
    

strs = ["flower","fow","flight"]
s = Solution()
print(s.longestCommonPrefix(strs))
