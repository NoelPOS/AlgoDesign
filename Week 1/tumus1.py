
input_num = int(input())
input_list = [0] * input_num

for i in range(input_num):
 user_in = int(input())
 input_list[i] = user_in

maximum = 0
temp = 0


for i in range( len(input_list) ):
 temp = max(temp + input_list[i], 0)

 if temp > maximum: 
  maximum = temp

print( maximum)
