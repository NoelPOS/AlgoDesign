import sys
sys.setrecursionlimit(10000)

p = list(map(int, input().split()))
L = len(p)
call = [0] * (L + 1)
mm = [None]*(L+1)

p.insert(0, 0)
count = 0


def maxRev(l):
    global p
    global count, call
    if mm[l] == None:
        call[l] += 1
        count += 1
        if l == 0:
            mm[l] = 0
        else:
            max_rev = -1
            for i in range(1, l+1):
                max_rev = max(max_rev, p[i] + maxRev(l-i))
            mm[l] = max_rev
    return mm[l]


print(maxRev(L))
print("Total Visits: ", count)
print("Calls: ", call)
print("memo" , mm)
