a = int(input())
b = int(input())
c = int(input())

if b != 0 and c != 0:
 temp = b * c
 result = a - temp
elif b == 0 and c != 0:
 result =  a - c
elif b != 0 and c == 0:
 result =  a - b
else: 
 result = 0

print(result)