#1 - 1,..., lengh of price inch
#2 - maxRev(l - index of price + 1) for price in prices

#3 - maxRev(l - index of price + 1) + price for price in prices

#4 and 5
count = 0
prices = list(map(int, input().split()))
def maxRev(length):
 global count
 count += 1
 if length <= 0:
  return 0
 max_rev = float('-inf')
 for i in range(1, len(prices) + 1):
  if i <= length:
   temp = maxRev(length - i) + prices[i - 1]
   max_rev = max(max_rev, temp)
 return max_rev

result = maxRev(len(prices))
print("Min Coins", result)
print("Recursion counts",count)

