import sys
sys.setrecursionlimit(1000000)

f , s = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

memo = {}
def lcs(i, j):
    if (i, j) in memo:
        return memo[(i, j)]
    if i == 0 or j == 0:
        memo[(i, j)] = 0
        return memo[(i, j)]
    else:
        if first[i - 1] == second[j - 1]:
            memo[(i, j)] = 1 + lcs( i - 1, j - 1)
            return memo[(i, j)]
        else:
            memo[(i, j)] = max(lcs(i - 1, j) , lcs(i, j - 1))
            return memo[(i, j)]

print(lcs(len(first), len(second)))
