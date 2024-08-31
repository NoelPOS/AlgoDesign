from sys import stdin

INF = 10000000000
V = int(input())
adj = [[] for i in range(V)]

for i in range(V + 1):
    x = input().split()
    u = int(x[0])
    v = int(x[1])
    w = int(x[2])
    adj[u].append((v,w))
    adj[v].append((u,w))

from simplePriorityQueue import Simple_Priority_Queue

class state:
    def __init__(self, city, d):
        self.city = city
        self.d = d

def successor(s):
    global shortest

    succ = []
    for a in adj[s.city]:
        v = a[0]
        w = a[1]
        if s.d + w < shortest[v]:
            shortest[v] = s.d + w
            succ.append(state(v, s.d+w))
    return succ

shortest = [INF]*V

def cityCompare(x, y):
    return x.d < y.d

# Write UCS code below this line
pq = Simple_Priority_Queue(cityCompare)
s = state(0, 0)
pq.enqueue(s)

while s.city != V - 1:
    for i in successor(s):
        pq.enqueue(i)
    s = pq.dequeue()

print(s.d)

            
        
        
        

















