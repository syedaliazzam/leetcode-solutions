class Solution:
    def reverseWords(self, s: str) -> str:
        r=s.split()
        res=" "
        for i in range(len(r)):
            res+=r[len(r)-1-i]+" "
        return res.strip()
            