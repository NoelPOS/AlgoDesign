a = int(input())
acts = []
for i in range(a):
 i = input().split()
 acts.append((int(i[0]), int(i[1])))

acts.sort(key=lambda x : x[1])

# for a in acts:
#  print(a)

lf = 0
c = 0

for s, f in acts:
 if s >= lf:
  c += 1
  lf = f

print(c)
