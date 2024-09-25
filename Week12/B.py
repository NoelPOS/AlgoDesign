def multiply2D(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]), (A[0][0] * B[0][1] + A[0][1] * B[1][1])],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]), (A[1][0] * B[0][1] + A[1][1] * B[1][1])]
    ]

def getExpo(M, n):
    if n == 1:
        return M
    if n % 2 == 0:
        half = getExpo(M, n // 2)
        return multiply2D(half, half)
    else:
        return multiply2D(M, getExpo(M, n - 1))


n = int(input())
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    M = [[1, 1], [1, 0]]
    result = getExpo(M, n - 1)
    F_n = result[0][0] * 1 + result[0][1] * 0

    return F_n

print(fib(n))


