v, e = map(int, input().split())
edges = []

for i in range(e):
    a, b, w = map(int, input().split())
    edges.append((w, a , b))

edges.sort()

from disjointsets3 import DisjointSets

djs = DisjointSets(v)
mst = 0
mst_edges = []
for e in edges:
    w, u , v = e
    if djs.findset(u) != djs.findset(v):
        mst += w
        mst_edges.append(e)
        djs.union(u, v)

print(mst)
print(mst_edges)



