N = int(input())
heights = list(map(int, input().split()))

def minCost(i):
    global heights
    if i == N:
        return 0
    else:
        firstJump = 0
        secondJump = 0
        if i + 1 < N:
            firstJump = abs(heights[i] - heights[i + 1]) + minCost(i + 1)
        if i + 2 < N:
            secondJump = abs(heights[i] - heights[i + 2]) + minCost(i + 2)
        return min(firstJump, secondJump)


print(minCost(0))
