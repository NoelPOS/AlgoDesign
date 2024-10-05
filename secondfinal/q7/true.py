import sys
sys.setrecursionlimit(10000)

villain = list(map(int, input().split()))
N = len(villain)
mm = {}

def minimalDmg(nVil):
    villianKey = tuple(nVil)
    
    # Check if the result for this configuration is already computed
    if villianKey in mm:
        return mm[villianKey]
    
    # Base case: if all villains are defeated
    if sum(nVil) == 0:
        result = 0
    else:
        dmg = float('inf')
        
        # Try to attack each villain
        for i in range(N):
            if nVil[i] != 0:
                nVil_copy = nVil.copy()
                
                # Defeat the villain and adjacent ones
                nVil_copy[(i-1) % N] = 0
                nVil_copy[i % N] = 0
                nVil_copy[(i+1) % N] = 0
                
                # Recursive call to find minimal damage
                dmg = min(minimalDmg(nVil_copy) + sum(nVil_copy), dmg)
        
        result = dmg
    
    # Memoize the result
    mm[villianKey] = result
    return result

print(minimalDmg(villain))
