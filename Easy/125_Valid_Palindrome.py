class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = [c.lower() for c in s if c.isalnum()]
        return ans == ans[::-1]
