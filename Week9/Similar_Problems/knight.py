import copy

n = int(input())
x = input().split()
sr = int(x[0])
sc = int(x[1])
x = input().split()
dr = int(x[0])
dc = int(x[1])

knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

class state:
    def __init__(self, row, col, step):
        self.r = row
        self.c = col
        self.step = step

def goal(s):
    return s.r == dr and s.c == dc

def valid(r, c):
    return 0 <= r < n and 0 <= c < n

def successor(s):
    succ = []
    for move in knight_moves:
        u = copy.deepcopy(s)
        u.r += move[0]
        u.c += move[1]
        if valid(u.r, u.c):
            u.step += 1
            succ.append(u)
    return succ

s = state(sr, sc, 0)
queue = []

while not goal(s):
    for u in successor(s):
        queue.append(u)
    s = queue[0]
    del queue[0]

print(s.step)
