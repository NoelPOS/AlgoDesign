from collections import deque

def knight_moves(start, end):
    moves = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
    start = (ord(start[0]) - 97, int(start[1]) - 1)
    end = (ord(end[0]) - 97, int(end[1]) - 1)
    
    queue = deque([(start[0], start[1], 0)])
    visited = set([start])
    
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == end:
            return dist
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))


T = int(input())
for _ in range(T):
    start, end = input().split()
    print(knight_moves(start, end))