import math

uin = int(input())
count = 0

while uin > 0:
 temp = int(math.sqrt(uin))
 square = temp ** 2
 uin -= square
 count += 1


print(count)
 
