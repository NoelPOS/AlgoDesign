# import sys
# sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())
memo = {}

def nWays(d, s):
    if (d, s) in memo:
        return memo[(d, s)]
    if d == L:
        if s == FLAT:
            return 1
        else:
            return 0
    else:
        counter = 0
        if s == FLAT:
            counter += nWays(d+1, UPPER2)
            # Actually, this is symmetric to UPPER2
            counter += nWays(d+1, LOWER2)
            if d < L-1:
                counter += nWays(d+2, FLAT)
        else:  # s is either UPPER2 or LOWER2
            counter += nWays(d+1, FLAT)
            if d < L-1:
                counter += nWays(d+2, s)
        memo[(d, s)] = counter
        return counter

for i in range(L -1, -1, -1):
    nWays(i, FLAT)

print(memo[(0, FLAT)])

# print(nWays(0, FLAT))