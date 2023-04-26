
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        
        if x == x[::-1]:
            return True
        else:
            return False
        
"""
https://leetcode.com/problems/palindrome-number/
int형 x가 Palindrome(앞뒤로 읽었을 때 같은 숫자)라면 True 아니라면 Flase

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false

숫자 앞에 다른게 붙으면 X
"""
