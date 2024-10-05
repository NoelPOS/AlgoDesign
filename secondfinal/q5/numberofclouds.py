r, c = list(map(int, input().split()))

cloud = []

for i in range(r):
    row = list(map(int, input().split()))
    cloud.append(row)


numberofclouds = 0
adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def valid(i, j):
    return 0 <= i < r and 0 <= j < c and cloud[i][j] == 1

for i in range(r):
    for j in range(c):
        if valid(i, j):
            numberofclouds += 1
            cloud[i][j] = 0
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                for a in adj:
                    newr, newc = x + a[0], y + a[1]
                    if valid(newr, newc):
                        cloud[newr][newc] = 0
                        stack.append((newr, newc))

print(numberofclouds)

