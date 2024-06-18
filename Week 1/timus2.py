def maximum_subrectangle_sum(matrix, N):
    max_sum = float('-inf')

    # Iterate over all pairs of columns (left_col, right_col)
    for left_col in range(N):
        temp = [0] * N  # temp array for each column pair
        for right_col in range(left_col, N):
            # Update temp array with cumulative sum from left_col to right_col for each row
            for row in range(N):
                temp[row] += matrix[row][right_col]

            # Apply Kadane's algorithm on temp to find maximum subarray sum
            current_sum = temp[0]
            max_temp = temp[0]
            for i in range(1, N):
                current_sum = max(temp[i], current_sum + temp[i])
                max_temp = max(max_temp, current_sum)

            # Update max_sum if we found a larger subrectangle sum
            if max_temp > max_sum:
                max_sum = max_temp

    return max_sum

# Reading input and processing
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
matrix = []
index = 1
for i in range(N):
    row = list(map(int, data[index:index + N]))
    matrix.append(row)
    index += N

# Calculate and print the maximum subrectangle sum
result = maximum_subrectangle_sum(matrix, N)
print(result)
