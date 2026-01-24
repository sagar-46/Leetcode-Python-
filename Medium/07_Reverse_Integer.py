class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = int(str(x)[::-1])
        res*=sign
        if res > 2 ** 31 -1 or res < -2 ** 31:
            return 0
        return res

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = abs(x)
        rev = 0
        while x > 0:
            rev = (rev * 10) + (x % 10)
            x //= 10
        if rev > 2 ** 31 -1:
            return 0
        return rev * sign
