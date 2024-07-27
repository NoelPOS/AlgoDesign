def minCost(i):
    if i == N-1:
        return 0
    if i >= N:
        return float('inf')
    
    cost1 = abs(stones[i] - stones[i+1]) + minCost(i+1) if i+1 < N else float('inf')
    cost2 = abs(stones[i] - stones[i+2]) + minCost(i+2) if i+2 < N else float('inf')
    
    return min(cost1, cost2)

N = int(input())
stones = list(map(int, input().split()))

print(minCost(0))
