import time

def Sum(x, i , j):
 s = 0
 for k in range (i, j + 1):
  s += x[k]
 return s

start = time.process_time()

input_list = list(map(int, input().split()))
maximum = 0
                  
for i in range(len(input_list)):
 for j in range(i, len(input_list)):
  result = Sum(input_list, i, j)
  maximum = max(maximum, result)


end = time.process_time()

print(maximum)
print("Process time: ", end - start)