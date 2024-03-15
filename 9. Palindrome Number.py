#Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            if x == int(str(x)[::-1]):
                return True
            else:
                return False   
        except ValueError:
            return False        


#########################################

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == int(str(x)[::-1]):
            return True
        else:
            return False               