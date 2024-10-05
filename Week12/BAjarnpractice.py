n = int(input())
m = 2147483647
M = [[1, 1], [1, 0]]

def multiply2D(A,B):
    C = [[A[0][0] * B[0][0] % m + A[0][1] * B[1][0] % m, 
          A[0][0] * B[0][1] % m + A[0][1] * B[1][1] % m],
         [A[1][0] * B[0][0] % m + A[1][1] * B[1][0] % m,
          A[1][0] * B[0][1] % m + A[1][1] * B[1][1] % m]]
    
    return C

def expo(M, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    else:
        half = expo(M, n // 2)
        if n % 2 == 0:
            return multiply2D(half, half)
        else:
            return multiply2D(M, multiply2D(half, half))
        
def fib(n):
    if n <= 1:
        return 1
    else:
        A = expo(M, n - 1)
        return (A[0][0] + A[0][1]) % m

print(fib(n))