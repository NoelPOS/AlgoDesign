import copy 

q = int(input())

class state():
    def __init__(self, q):
        self.queens = [-1] * q
        self.col = 0

def goal(s):
    if s.col == q:
        return True
    return False

def conflict(Q, i, j):
    if Q[i] == Q[j] or abs(Q[i]-Q[j]) == abs(i-j):
        return True
    return False

def valid(s):
    for i in range(s.col):
        if conflict(s.queens, i, s.col):
            return False
    return True


def successor(s):
    succ = []
    for i in range(q):
        u = copy.deepcopy(s)
        u.queens[u.col] = i
        if valid(u):
            u.col += 1
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
Q = []

while not goal(s):
    for u in successor(s):
        Q.append(u)
    s = Q[0]
    del Q[0]

printqueens(s.queens)
