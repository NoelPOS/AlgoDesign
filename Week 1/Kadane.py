input_list = list(map(int, input().split()))

maximum = 0
temp = 0


for i in range( len(input_list) ):
 temp = max(temp + input_list[i], 0)
 print("input", input_list[i])
 if temp > maximum: 
  maximum = temp
 



print("Maximum: ", maximum)
