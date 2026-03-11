class Solution:
    def isPalindrome(self, s: str) -> bool:

        o=''.join([i.lower() for i in s if i.isalnum()])

        return o==o[::-1]

        