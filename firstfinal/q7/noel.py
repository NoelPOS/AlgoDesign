M, N = map(int, input().split())  

w = []  # Stock prices
v = []  # Stock profits

for _ in range(N):
    price, profit = map(int, input().split())
    w.append(price)
    v.append(profit)

count = 0  


memo = [[-1] * (M + 1) for _ in range(N + 1)]

def maxVal(i, C):
    global count
    if memo[i][C] != -1:
        return memo[i][C]
    else: 
        count += 1  # Track the number of function calls
        if i == N:  # Base case: no more items to consider
            memo[i][C] = 0
            return memo[i][C]
        else:
            skip = maxVal(i + 1, C)
            if w[i] <= C:
                take = v[i] + maxVal(i + 1, C - w[i])
            else:
                take = -1  
            memo[i][C] = max(skip, take)
            return memo[i][C]


result = maxVal(0, M)
print(result)

