import heapq

p = list(map(int, input().split()))

pq = []
for i in p:
    heapq.heappush(pq, i)

totalcost = 0
while len(pq) > 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    totalcost += a + b
    heapq.heappush(pq, a + b)

print(totalcost)
    


