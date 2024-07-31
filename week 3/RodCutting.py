#1 - 1,..., lengh of price inch
#2 - maxRev(l - index of price + 1) for price in prices

#3 - maxRev(l - index of price + 1) + price for price in prices

#4 and 5
# count = 0
# prices = list(map(int, input().split()))
# def maxRev(length):
#  global count
#  count += 1
#  if length <= 0:
#   return 0
#  max_rev = float('-inf')
#  for i in range(1, len(prices) + 1):
#   if i <= length:
#    temp = maxRev(length - i) + prices[i - 1]
#    max_rev = max(max_rev, temp)
#  return max_rev

# result = maxRev(len(prices))
# print("Min Coins", result)
# print("Recursion counts",count)

import sys
sys.setrecursionlimit(10000)

p = input().split()
L = len(p)
for i in range(L):
    p[i] = int(p[i])
p.insert(0, 0)

memo = [None] * (L + 1)

def maxRev(l):
    global p,L

    if memo[l] != None:
        return memo[l]
    if l == 0:
        memo[l] = 0
        return memo[l]
    else:
        mx = float('inf')
        for i in range(1, l + 1):
            if i <= L and p[i] != -1:
                mx = min(mx, p[i] + maxRev(l - i))  
        memo[l] = mx
        return memo[l]    
print(maxRev(L))