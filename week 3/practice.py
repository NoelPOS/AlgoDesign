coins = list(map(int, input().split()))
change = int(input())
answer = float('inf')
def mincoin(v):
 global answer
 if v <= 0:
  return 0
 else:
  for coin in coins:
   diff = v - coin
   result = 1 + mincoin(diff)
   answer = min(answer, result)

mincoin(change)
print(answer)