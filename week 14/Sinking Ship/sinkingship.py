N = int(input())
floors = []
for i in range(N):
    floors.append(list(map(int, input().split())))

class state():
    def __init__(self, value):
        self.value = value

from simplePriorityQueue import Simple_Priority_Queue

def valuecompare(x, y):
    return x.value > y.value

s = state(0)
pq = Simple_Priority_Queue(valuecompare)
max = 0

for i in range(N):
    for v in floors[i]:
        a = state(v)
        pq.enqueue(a)
    m = pq.dequeue()
    max += m.value

print(max)
    
