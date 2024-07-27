import sys
sys.setrecursionlimit(10000)

N,M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

mm = [[-1]*(M+1) for i in range(N+1)]


# for i in range(N + 1):
#     mm[i][0] = 0

# for j in range(M + 1):
#     mm[0][j] = 0


# for i in range(1, N + 1):
#     for j in range(1, M + 1):
#         if w[i - 1] <= j:
#             mm[i][j] = max(mm[i - 1][j], mm[i -1][j - w[i - 1]] + v[i - 1])
#         else:
#             mm[i][j] = mm[i - 1][j]
# print(mm[N][M])

def maxVal(i,C):
    if mm[i][C] == -1:
        if i == N or C == 0:
            mm[i][C] = 0
        else:
            skip = maxVal(i+1, C)   # skip item i
            take = 0
            if w[i] <= C:
                take = v[i] + maxVal(i+1, C-w[i])  # take item i
            mm[i][C] = max(skip,take)
    return mm[i][C]

for i in range(N -1, -1, -1):
    for j in range(M + 1):
        mm[i][j] = maxVal(i,j)

print(mm[0][M])