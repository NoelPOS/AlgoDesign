import sys
sys.setrecursionlimit(10001)

c = list(map(int, input().split()))
V = int(input())
call = [0] * (V + 1)
mm = [None] * (V + 1)

print(mm)


def mincoin_non_recursive(V, c):
    mm[0] = 0  # Base case
    for v in range(1, V + 1):
        minc = float('inf')
        for x in c:
            print("outside", mm)
            if x <= v:
                minc = min(minc, 1 + mm[v - x])
        mm[v] = minc
        print("inside", mm)


# Call the non-recursive function
mincoin_non_recursive(V, c)
print(mm[V])
