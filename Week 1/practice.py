A = list(map(int, input().split()))


# def Sum(x, i, j):
#  s = A[j] - A[i]
#  return s

# for i in range(1, len(A)):
#  A[i] = A[i - 1] + A[i]


# maxsum = float('-inf')

# for i in range(len(A)):
#  for j in range(i, len(A)):
#   temp = Sum(A, i, j)
#   if temp > maxsum:
#    maxsum = temp
# print(maxsum)

maxsum = 0
temp = 0
for i in A:
 temp = max(0, temp + i)
 if temp > maxsum:
  maxsum = temp

print(maxsum)