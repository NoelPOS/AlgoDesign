import time

def Sum(x, i , j):
 s =  x[j]
 if i > 0:
  s -= x[i - 1]
 return s

start = time.process_time()

input_list = list(map(int, input().split()))
# i = 0
# j = 1
# while i < len(input_list) - 1  and j < len(input_list)  :
#  temp = input_list[i] + input_list[j]
#  input_list[j] = temp
#  i += 1
#  j += 1

for i in range(len(input_list) - 1):
 input_list[i + 1] = input_list[i] + input_list[i + 1]

print(input_list)

 

maximum = 0
for i in range(len(input_list)):
 for j in range(i, len(input_list)):
  result = Sum(input_list, i, j)
  maximum = max(maximum, result)

end = time.process_time()

print(maximum)
print("Process time: ", end - start)