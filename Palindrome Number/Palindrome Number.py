#https://leetcode.com/problems/palindrome-number/description/

# How to solve it:
# 1. Convert the number to a string
# 2. Compare the string with its reverse
# 3. If they are the same, return True
# 4. Otherwise, return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
# Time complexity: O(n)
# Space complexity: O(1)
        
        