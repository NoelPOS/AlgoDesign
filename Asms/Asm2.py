def minCost(k, prices, memo):
    if k == 0:
        return 0
    if k in memo:
        return memo[k]

    min_cost = float('inf')
    for i in range(1, k + 1):
        if prices[i - 1] != -1:
            cost = minCost( k - i, prices, memo)
            if cost != float('inf'):
                min_cost = min(min_cost, cost + prices[i - 1])
    memo[k] = min_cost
    return min_cost

tests = int(input())
results = []
for i in range(tests):
 n, k = list(map(int, input().split()))
 prices = list(map(int, input().split()))
 results.append(minCost( k, prices, {}))
    
for i in results:
    if i == float('inf'):
        print(-1)
    else:
        print(i)