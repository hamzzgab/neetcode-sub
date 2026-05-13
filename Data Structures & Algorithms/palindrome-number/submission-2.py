class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        reversed_num = 0
        decrement = x
        temp = 0
        while decrement > 0:
            reversed_num *= 10
            temp = decrement % 10
            decrement //= 10
            reversed_num += temp
            
        return reversed_num == x