# LetterA = input()
# LetterB = input()

# A = len(LetterA)
# B = len(LetterB)

# dp = [[0 for i in range(B+1)] for j in range(A+1)]

# for i in range(A+1):
#     for j in range(B+1):
#         if i == 0:
#             dp[i][j] = j
#         elif j == 0:
#             dp[i][j] = i
#         elif LetterA[i-1] == LetterB[j-1]:
#             dp[i][j] = dp[i-1][j-1]
#         else:
#             dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])   

# for i in dp:
#     print(i)
# print(dp[A][B])

# import sys
# sys.setrecursionlimit(1000000)

# LetterA = input()
# LetterB = input()

# A = len(LetterA)
# B = len(LetterB)
# memo = [[None for i in range(B+1)] for j in range(A+1)]
# def editDistance(a, b):
#     if memo[a][b] != None:
#         return memo[a][b]
#     if a == len(LetterA):
#         memo[a][b] = len(LetterB) - b
#         return memo[a][b]
#     if b == len(LetterB):
#         memo[a][b] = len(LetterA) - a
#         return memo[a][b]
#     if LetterA[a] == LetterB[b]:
#         memo[a][b] = editDistance(a+1, b+1)
#         return memo[a][b]
#     else:
#         memo[a][b] = 1 + min(editDistance(a, b+1), editDistance(a+1, b), editDistance(a+1, b+1))
#         return memo[a][b]
    
# print(editDistance(0, 0))

def editDistance_dp(a, b):
    m = len(a)
    n = len(b)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                              dp[i][j - 1] + 1,  # Insertion
                              dp[i - 1][j - 1] + 1)  # Substitution

    return dp[m][n]

a = input()
b = input()
print(editDistance_dp(a, b))




