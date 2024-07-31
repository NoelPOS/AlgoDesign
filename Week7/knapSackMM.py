N , M = map(int, input().split())

w = list(map(int, input().split()))
v = list(map(int, input().split()))
count = 0

memo = [[-1] * (M + 1) for i in range(N + 1)]

def maxVal(i, C):
 global count
 if memo[i][C] != -1:
  return memo[i][C]
 else: 
   count += 1
   if i == N:
      memo[i][C] = 0
      return memo[i][C]
   else:
      skip = maxVal(i + 1, C)
      if w[i] <= C:
         take = v[i] + maxVal(i + 1, C - w[i])
      else:
         take = -1
      memo[i][C] =  max(skip, take)
      return memo[i][C] 
 
# print(maxVal(0, M))
for i in range(N , -1, -1):
  for j in range(M + 1):
    memo[i][j] = maxVal(i, j)
print(memo[0][M])
print(count)


#ACUTUAL DYNAMIC PROGRAMMING SOLUTION

# for i in range(N + 1):
#  memo[i][0] = 0

# for i in range(M + 1):
#  memo[0][i] = 0
 
# for i in range(1, N + 1):
#  for j in range(1, M + 1):
#   if w[i - 1] <= j:
#    memo[i][j] = max(memo[i - 1][j], v[i - 1] + memo[i - 1][j - w[i - 1]])
#   else:
#    memo[i][j] = memo[i - 1][j]

# print(memo[N][M])