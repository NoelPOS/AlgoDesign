#1
# coins = list(map(int, input().split()))
# change = int(input())

#2
# a. every item in coins
# b. change - item for item in coins
# c. mincoin(v - i) for i in items
# d. 1 + mincoin(v - i) for i in items
# e. 0

#3 and 4
# count = 0
# def minCoin(change):
#  global count
#  count += 1
#  mincoin = float('inf')
#  if change <= 0:
#   return 0
#  for coin in coins:
#   if coin <= change:
#    temp = minCoin(change - coin) + 1
#    mincoin = min(mincoin, temp)
 
#  return mincoin
  
# result = minCoin(change)
# print("Min Coins", result)
# print("Recursion counts",count)


import sys
sys.setrecursionlimit(10000)

c = input().split()
V = int(input())

for i in range(len(c)):
    c[i] = int(c[i])

memo = [None] * (V + 1)

def mincoin(v):
    global c
    if memo[v] != None:
        return memo[v]
    if v == 0:
        memo[v] = 0
        return memo[v]
    else:
        answer = float('inf')
        for coin in c:
          if coin <=v:
            diff = v - coin
            result = 1 + mincoin(diff)
            answer = min(answer, result)
        memo[v] = answer
        return memo[v]
    
print(mincoin(V))






