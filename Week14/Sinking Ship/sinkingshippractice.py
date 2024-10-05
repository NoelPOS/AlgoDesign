f = int(input())
floors = []
for i in range(f):
    floors.append(list(map(int, input().split())))

from simplePriorityQueue import Simple_Priority_Queue

def mycompare(x, y):
    return x > y

pq = Simple_Priority_Queue(mycompare)
total = 0

for i in range(f):
    for j in floors[i]:
        pq.enqueue(j)
    s = pq.dequeue()
    total += s

print(total)



