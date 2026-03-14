class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if 3 * 2 ** (n - 1) < k:
            return ""
        
        made, ans = 0, ''
        def backtrack(i, prev_letter):
            nonlocal made, ans
            if i == n - 1:
                # We created a happy string
                made += 1
                # Check to see if it is the kth happy string
                if made == k:
                    return True
                return False
            
            letters = (s for s in 'abc' if s != prev_letter)
            for l in letters:
                if backtrack(i + 1, l):
                    # Insert the letters of the kth happy string
                    ans += l
                    return True
            return False
        
        backtrack(-1, 'd')

        # Our ans is appended in reverse
        return ans[::-1]