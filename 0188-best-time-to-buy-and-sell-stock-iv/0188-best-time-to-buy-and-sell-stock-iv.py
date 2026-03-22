class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # DP table: dp[day][buy_state][transactions_left]
        dp = [[[-1]*(k+1) for _ in range(2)] for _ in range(n)]

        def solve(ind, buy, k):
            # Base case: no more days
            if ind == n:
                return 0
            
            # Base case: no transactions left
            if k == 0:
                return 0

            # Return cached result if already computed
            if dp[ind][buy][k] != -1:
                return dp[ind][buy][k]

            if buy == 1:  # Can buy stock
                take = -prices[ind] + solve(ind+1, 0, k)
                not_take = solve(ind+1, 1, k)
                dp[ind][buy][k] = max(take, not_take)
            else:  # Holding stock, can sell
                sell = prices[ind] + solve(ind+1, 1, k-1)  # Complete transaction
                skip = solve(ind+1, 0, k)  # Keep holding
                dp[ind][buy][k] = max(sell, skip)
            
            return dp[ind][buy][k]

        return solve(0, 1, k)