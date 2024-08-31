import copy

x = list(map(int, input().split()))
rows = x[0]
cols = x[1]
y = list(map(int,input().split()))
sr = y[0]
sc = y[1]
z = list(map(int,input().split()))
dr = z[0]
dc = z[1]

matrix = [[0 for c in range(cols)] for r in range(rows)]
adj = [(0,1), (1,0), (-1,0), (0, -1)]

for i in range(rows):
   temp = list(map(int, input().split()))
   for j in range(cols):
      matrix[i][j] = -int(temp[j])


class state():
   def __init__(self, r, c, steps):
      self.r = r
      self.c = c
      self.steps = steps

def goal(s):
   if s.r == dr and s.c == dc:
       return True
   return False

def valid(r , c):
   if r >= 0 and r < rows and c >= 0 and c < cols:
      if matrix[r][c] == 0:
         return True
   return False

def successor(s):
   succ = []
   for a in adj:
      u = copy.deepcopy(s)
      u.r += a[0]
      u.c += a[1]
      if valid(u.r, u.c):
         u.steps += 1
         matrix[u.r][u.c] = u.steps
         succ.append(u)

   return succ
   
s = state(sr, sc, 0)
queue = []

while not goal(s):
   for x in successor(s):
      queue.append(x)
   s = queue[0]
   del queue[0]

print(s.steps)


      

