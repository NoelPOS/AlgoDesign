a = int(input())
x = int(input())

def halfexpo(a, x):
    if x == 0:
        return 1
    if x == 1:
        return a
    if x % 2 == 0:
        half = halfexpo(a, x //2)
        return half * half
    if x % 2 != 0:
        half = halfexpo(a, x //2)
        return half * half * a
    
print(halfexpo(a, x)) 

# time complexity: O(log n)
# reason: the function is called recursively and the input is halved each time.
# the function is called log n times.


    