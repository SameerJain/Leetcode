class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_str = []
        for c in s:
            if c.isalnum():
                new_str.append(c)
        

        new_str = ''.join(new_str).lower()

        l = 0
        r = len(new_str) - 1
        
        while l <= r:
            if new_str[l] != new_str[r]:
                return False
            l += 1
            r -= 1
        return True 