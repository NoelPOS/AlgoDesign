n = int(input())

act = []
for i in range(n):
    act.append(list(map(int, input().split())))

def mysort(x):
    return x[1]

act.sort(key=mysort)

count = 0
lf = -1

for a in act:
    if a[0] > lf:
        count += 1
        lf = a[1]
print(count)


