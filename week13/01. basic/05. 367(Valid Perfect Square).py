from math import sqrt, floor

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if ((num ** 0.5) % 1 == 0):
            return True
        return False

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return sqrt(num) == floor(sqrt(num))