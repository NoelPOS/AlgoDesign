n = int(input())
act = []

for i in range(n):
    act.append(list(map(int, input().split())))


act.sort(key=lambda x: x[1])

print(act)

lf = -1
count = 0

for a in act:
    if a[0] > lf:
        count += 1
        lf = a[1]

print(count)


