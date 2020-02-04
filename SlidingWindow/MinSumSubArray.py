import sys
INT_MAX = sys.maxsize

def findSubarray(arr, k):
    n = len(arr)
    
    if k > n:
        print("Size of subarray cannot be greater than the array itself")
        return
    
    cur_sum = sum([arr[i] for i in range(k)])
    min_sum = INT_MAX
    start = 0

    for i in range(n-k):
        cur_sum = cur_sum - arr[i] + arr[i+k]
        if cur_sum < min_sum:
            min_sum = cur_sum
            start = i + 1
    
    return arr[start:start+k]

arr = [10, 4, 2, 5, 6, 3, 8, 1]
print(findSubarray(arr, 3))