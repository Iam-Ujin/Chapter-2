# n = int(input())
# tri = []
# for _ in range(n):
#     tri.append(list(map(int, input().split())))
#
# dp = [[0] * (i + 1) for i in range(n)]
#
# dp[0][0] = tri[0][0]
#
# for i in range(0, len(tri)-1):
#     for j in range(len(tri[i])):
#         dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + tri[i + 1][j])
#         dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + tri[i + 1][j + 1])
#
# print(max(dp[-1]))





def solution(triangle):
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(0, len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

    return (max(dp[-1]))
