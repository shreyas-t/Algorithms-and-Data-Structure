# https://www.techiedelight.com/find-subarray-having-given-sum-given-array/

def findSubarray(arr, sum):
    n = len(arr)

    window_sum = 0
    end = 0

    for start in range(n):
        
        while window_sum < sum and end< n:
            window_sum += arr[end]
            end += 1
        
        if(window_sum == sum):
            print(arr[start:end])
        
        window_sum -= arr[start]


arr =  [2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
sum = 15
findSubarray(arr, sum)