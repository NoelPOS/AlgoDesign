N = list(map(int, input().split()))

maximum = 0
curr = 0

for i in range(len(N)):
 curr = max(curr + N[i], 0)
 maximum = max(maximum, curr)
 
print("Maximum: ", maximum)
