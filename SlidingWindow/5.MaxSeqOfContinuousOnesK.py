# https://www.techiedelight.com/find-maximum-sequence-of-continuous-1s-can-formed-replacing-k-zeroes-ones/

def longestSeq(arr, k):
    n = len(arr)
   
    if k > n:
        print("Longest sequence cannot be greater than the array itself")
        return 
    
    start = 0
    end = 0
    max_start = 0
    max_end = 0
    count_zero = 0

    for i in range(n):
        end += 1
            
        if arr[i] == 0:
            count_zero += 1

        while count_zero > k:
            while arr[start] != 0:
                start += 1
            start += 1
            count_zero -= 1
        
        if end - start > max_end-max_start:
            max_start = start
            max_end = end
    
    return max_start, max_end-1

arr = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0]
print(longestSeq(arr, 2))

 
