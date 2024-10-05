N = int(input())
itensities = [0] * N
for i in range(N):
    itensities[i] = int(input())


maximum = 0
curr = 0

for i in range(N):
    curr = max(0, curr + itensities[i])
    maximum = max(maximum, curr)

print(maximum)