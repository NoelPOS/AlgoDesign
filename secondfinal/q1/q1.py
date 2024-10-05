from disjointsets3 import DisjointSets

v,e = map(int, input().split())
edges = []

for i in range(e):
    u, v , w = map(int, input().split())
    edges.append((w,u,v))

edges.sort()

ds = DisjointSets(v + 1)
mst = 0
mst_edges = []

for w, u, v in edges:
    if ds.findset(u) != ds.findset(v):
        ds.union(u,v)
        mst += w
        mst_edges.append((u,v))

print(mst)
print(mst_edges)

