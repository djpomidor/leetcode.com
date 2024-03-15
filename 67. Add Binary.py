# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = ""
        for i in range(len(a)):
            sum = bin(int(a[i])) + bin (int(b[i]))
            print("!!!", sum)
        return sum
    # str = "asdf" [::-1]



a = "1010"
b = "1011"

str = Solution()

print(str.addBinary(a,b))