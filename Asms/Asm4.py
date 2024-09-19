puzzle = []

for i in range(3):
    row = list(map(int, input().split()))
    puzzle.append(row)
adj = [(0, 1), (1, 0), (0, -1), (-1, 0)]

import copy


class state():
    def __init__(self, puzzle, steps):
        self.puzzle = puzzle
        self.steps = steps


def goal(s):
    if s.puzzle == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
        return True
    return False

def getempty(s):
    for i in range(3):
        for j in range(3):
            if s.puzzle[i][j] == 0:
                return i, j
            
def valid(r, c):
    if r >= 0 and r < 3 and c >= 0 and c < 3:
        return True
    return False

def successor(s):
    succ = []
    er, ec = getempty(s)
    for a in adj:
        u = copy.deepcopy(s)
        nr = er + a[0]
        nc = ec + a[1]
        if valid(nr, nc):
            u.puzzle[er][ec], u.puzzle[nr][nc] = u.puzzle[nr][nc], u.puzzle[er][ec]
            u.steps += 1
            succ.append(u)
    return succ


s = state(puzzle, 0)
queue = [s]

while not goal(s):
    for x in successor(s):
        queue.append(x)
    s = queue[0]
    del queue[0]

print(s.steps)