import sys

sys.setrecursionlimit(100000)

coins = list(map(int, input().split()))
change = int(input())

memo = [-1] * (change + 1)
memoCount = [0] * (change + 1)
count = 0

def minCoin(i): 
    global count
    count += 1
    if memo[i] != -1:
        memoCount[i] += 1
        return memo[i]
    elif i == 0:
        memo[i] = 0
        return memo[i]
    else:
        min_coin = float('inf')
        for coin in coins:
            if coin <= i:
                min_coin = min(min_coin, 1 + memo[i - coin])
        memo[i] = min_coin
        return memo[i]
   
for i in range(change + 1):
    minCoin(i)
print("Result ", memo[change])
print("memoCount" , memoCount)
print("recursionCount" , count)


#ACTUAL DYNAMIC PROGRAMMING SOLUTION

# import sys
# sys.setrecursionlimit(10001)

# c = list(map(int, input().split()))
# V = int(input())
# call = [0] * (V + 1)
# mm = [None] * (V + 1)

# print(mm)

# def mincoin_non_recursive(V, c):
#     mm[0] = 0  # Base case
#     for v in range(1, V + 1):
#         minc = float('inf')
#         for x in c:
#             print("outside", mm)
#             if x <= v:
#                 minc = min(minc, 1 + mm[v - x])
#         mm[v] = minc
#         print("inside", mm)

# Call the non-recursive function
# mincoin_non_recursive(V, c)
# print(mm[V])