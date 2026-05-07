class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        change = 0
        while l < r:
            if s[l] != s[r]:
                r -= 1
                change += 1
            else:
                l += 1
                r -= 1

        print(change)
        if change > 1:
            change = 0
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    l += 1
                    change += 1
                else:
                    l += 1
                    r -= 1
                    
            if change <= 1:
                return True
        elif change <= 1:
            return True
        return False

            