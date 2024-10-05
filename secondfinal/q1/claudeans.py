from disjointsets3 import DisjointSets

def capital_centered_network(n, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize DisjointSets
    ds = DisjointSets(n)
    
    total_cost = 0
    connected_cities = set([0])  # Start with the capital (city 0)
    
    for u, v, w in edges:
        # Check if one city is in the connected set and the other isn't
        if (u in connected_cities) != (v in connected_cities):
            if ds.findset(u) != ds.findset(v):
                ds.union(u, v)
                total_cost += w
                connected_cities.add(u)
                connected_cities.add(v)
        
        # If all cities are connected, we're done
        if len(connected_cities) == n:
            break
    
    return total_cost

# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and print the result
result = capital_centered_network(n, edges)
print(result)