#https://leetcode.com/problems/palindrome-number/description/

# By Converting String
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


        
        