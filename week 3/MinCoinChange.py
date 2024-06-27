#1
coins = list(map(int, input().split()))
change = int(input())

#2
# a. every item in coins
# b. change - item for item in coins
# c. mincoin(v - i) for i in items
# d. 1 + mincoin(v - i) for i in items
# e. 0

#3 and 4
count = 0
def minCoin(change):
 global count
 count += 1
 mincoin = float('inf')
 if change <= 0:
  return 0
 for coin in coins:
  if coin <= change:
   temp = minCoin(change - coin) + 1
   mincoin = min(mincoin, temp)
 
 return mincoin
  
result = minCoin(change)
print("Min Coins", result)
print("Recursion counts",count)


