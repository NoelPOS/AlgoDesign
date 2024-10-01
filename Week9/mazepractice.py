import copy 


x = input().split()
M = int(x[0])    # number of rows
N = int(x[1])    # number of columns
maze = [[0 for i in range(N)] for j in range(M)]
x = input().split()
sr = int(x[0])
sc = int(x[1])
x = input().split()
dr = int(x[0])
dc = int(x[1])
for i in range(M):
    x = input().split()
    for j in range(N):
        maze[i][j] = -int(x[j])

Adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class state():
    def __init__(self, r, c, step):
        self.r = r
        self.c = c
        self.step = step


def goal(s):
    if s.r == dr and s.c == dc:
        return True
    return False

def valid(s):
    if 0 <= s.r < M and 0 <= s.c < N:
        if maze[s.r][s.c] == 0:
            return True
    return False

def successor(s):
    succ = []
    for a in Adj:
        u = copy.deepcopy(s)
        u.r += a[0]
        u.c += a[1]
        if valid(u):
            u.step += 1
            maze[u.r][u.c] = u.step
            succ.append(u)

    return succ


s = state(sr, sc, 0)
Q = []

while not goal(s):
    for i in successor(s):
        Q.append(i)

    s = Q[0]
    del Q[0]

print(s.step)



