class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        def findPals(i):
            # find palindromes starting at i
            for j in range(n-i-1,-1,-1):
                for k in range(j//2+1):
                    if s[i+k] != s[i+j-k]:
                        break
                else:
                    yield s[i:i+j+1]

        @cache
        def helper(i):
            # determines minimum number of slices necessary for s[i:]
            if i == n-1:
                return 0
            if i == n:
                return -1
            pals = findPals(i)
            best = n+1
            for p in pals:
                x = helper(i+len(p))
                best = min(best, x)
                if x<= 0:
                    break

            return best+1

        return helper(0)