from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for digit in digits:
            number = number*10 + digit
        number = number + 1
        print("!!", number)
        return [int(digit2) for digit2 in str(number)]

mylist = [1,2,3]
s = Solution()
print(s.plusOne(mylist))
