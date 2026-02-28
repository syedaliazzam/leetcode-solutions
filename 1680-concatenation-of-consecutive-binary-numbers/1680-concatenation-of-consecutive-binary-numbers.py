class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 1_000_000_007
        curBits = 0
        output = 0
        
        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                curBits += 1
            output = ((output << curBits) | i) % MOD
            
        return output