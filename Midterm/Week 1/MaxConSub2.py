import time

def Sum(x, i , j):
 s =  x[j]
 if i > 0:
  s -= x[i - 1]
 return s

start = time.process_time()

N = list(map(int, input().split()))

for i in range(len(N) - 1):
 N[i + 1] = N[i] + N[i + 1]

maximum = 0
for i in range(len(N)):
 for j in range(i, len(N)):
  result = Sum(N, i, j)
  maximum = max(maximum, result)

end = time.process_time()

print(maximum)
print("Process time: ", end - start)