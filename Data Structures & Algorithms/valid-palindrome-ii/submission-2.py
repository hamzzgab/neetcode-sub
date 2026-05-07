class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(l, r, deleted):
            if l >= r:
                return True

            if s[l] != s[r]:
                if not deleted:
                    return palindrome(l + 1, r, True) or palindrome(l, r -1, True)            
                else:
                    return False

            return palindrome(l + 1, r - 1, deleted)
        return palindrome(0, len(s) - 1, False)
