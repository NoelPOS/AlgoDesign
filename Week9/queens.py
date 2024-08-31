import copy
q = int(input())

def conflict(Q, i, j):
    if Q[i] == Q[j] or abs(Q[i]-Q[j]) == abs(i-j):
        return True
    return False

class state():
    def __init__(self, n):
        self.queen = [-1]*n
        self.c = 0

def goal(s):
    if s.c == q:
        return True
    return False

def valid(u):
    for i in range(u.c):
        if conflict(u.queen, i, u.c):
            return False
    return True

def successor(s):
    succ = []
    for r in range(q):
        u = copy.deepcopy(s)
        u.queen[u.c] = r
        if valid(u):
            u.c += 1
            succ.append(u)

    return succ

def printqueens(Q):
    n = len(Q)
    board = [['.']*n for i in range(n)]
    for j in range(n):
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()

s = state(q)
Q =[]

while not goal(s):
    for u in successor(s):
        Q.append(u)
    s = Q[0]
    del Q[0]


printqueens(s.queen)








