def partition(arr, left, right):
    # Choose the pivot element
    pivot = arr[right]
    i = left - 1

    # Partition the array into elements <= pivot and elements > pivot
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            # Swap elements arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot element in its correct position
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def ksmallest(arr, l, r, k):
    if l == r:
        return arr[l]
    else:
        pivot = partition(arr, l, r)
        if pivot < k:
            return ksmallest(arr, pivot + 1, r, k)
        elif pivot > k:
            return ksmallest(arr, l, pivot - 1, k)
        else:
            return arr[pivot]

arr = list(map(int, input().split()))
k = int(input())
print(ksmallest(arr, 0, len(arr) - 1, k - 1))



