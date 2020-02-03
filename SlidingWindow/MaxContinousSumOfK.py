import sys

MIN_INT = -sys.maxsize-1

def maxSum(arr, n, k):
    if k>n:
        raise ValueError("Window size can't be greater than array size")

    max_sum = MIN_INT
    window_sum = sum([arr[i] for i in range(k)])

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[k+i]
        max_sum = max(window_sum, max_sum)

    return max_sum 

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20] 
k = 4
n = len(arr) 
print(maxSum(arr, n, k)) 