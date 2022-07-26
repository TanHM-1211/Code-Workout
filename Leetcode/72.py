class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # if m == 0 or n == 0:
        #     return max(m, n) - min(m, n)

        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min([
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    ])
        
        return dp[m][n]

while True:
    word1 = input()[1:-1]
    word2 = input()[1:-1]
    print(Solution().minDistance(word1, word2))

