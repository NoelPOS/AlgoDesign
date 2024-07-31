import sys
sys.setrecursionlimit(100000)

N, K , S = map(int, input().split())

balls = [None] * N
for i in range(N):
    pos, score = map(int, input().split())
    balls[i] = [pos, score]


memo = {}

def quickSilver(i, K , S):
    global balls
    if (i, K, S) in memo:
        return memo[(i, K, S) ]
    else:
        if i == N:
            memo[(i, K, S) ] = 0
            return memo[(i, K, S) ]
        else:
            if abs(S - balls[i][0]) <= K:
                leave = 0 + quickSilver(i + 1, K, S)
                take = balls[i][1] + quickSilver(i + 1, K, balls[i][0])
                memo[(i, K, S) ] = max(leave, take)
                return memo[(i, K, S) ]
            else:
                memo[(i, K, S) ] = quickSilver(i + 1, K, S)
                return memo[(i, K, S)]
        
        
    
    
print(quickSilver(0, K, S))
