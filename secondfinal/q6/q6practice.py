L = int(input())
MOD = 44711

def multiply2D(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, 
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]

def expo(M, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    else:
        mhalf = expo(M, n // 2)
        if n % 2 == 0:
            return multiply2D(mhalf, mhalf)
        else:
            return multiply2D(multiply2D(mhalf, mhalf), M)


def tile(L):
    if L % 2 == 1:
        return 0
    if L == 0:
        return 1
    if L == 2:
        return 3
    
    M = [[4, -1], [1, 0]]
    A = expo(M, L // 2 - 1)

    return (3 * A[0][0] + A[0][1]) % MOD

print(tile(L))