import copy 

def printqueens(Q):
    n = len(Q)
    board = [['.']*n for i in range(n)]
    for j in range(n):
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()

def conflict(Q, i, j):
    if Q[i] == Q[j] or abs(Q[i]-Q[j]) == abs(i-j):
        return True
    return False

# s = initial_state
# while not Goal(s)
# for each successor_state x of s 
# enqueue(x)
# s = dequeue()

q = int(input())

class state():
    def __init__(self, q):
        self.queens = [-1] * q # [-1, -1, -1, -1, -1]
        self.col = 0

s = state(q)
queue = []

def goal(s):
    return s.col == q

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

while not goal(s):
    for s in successor(s):
        queue.append(s)
    s = queue[0]
    del queue[0]

printqueens(s.queens)

