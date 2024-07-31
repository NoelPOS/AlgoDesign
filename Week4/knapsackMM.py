N , M = map(int, input().split())

w = list(map(int, input().split()))
v = list(map(int, input().split()))
count = 0

memo = [[-1] * (M + 1) for i in range(N + 1)]
call = [[0] * (M + 1) for i in range(N + 1)]

def maxVal(i, C):
 global count
 if memo[i][C] != -1:
  return memo[i][C]
 else: 
  count += 1
  call[i][C] += 1
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
 
print("Result", maxVal(0, M))
print("Count", count)
print("Calls", call)