# https://www.techiedelight.com/find-maximum-length-sequence-continuous-ones-sliding-window/

def findIndexOfZero(arr):
    n = len(arr)

    start = 0
    end = 0
    count_zero = 0
    index = 0
    max_size = 1

    for i in range(n):
        end += 1

        if arr[i] == 0:
            count_zero += 1
            prev_index_zero = i
        
        if count_zero >1:
            while(arr[start] != 0):
                start += 1
            start+=1
            count_zero -= 1
        
        if end - start > max_size:
            max_size = end-start
            index = prev_index_zero

    print(arr[start:end])
    return index

arr = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1 ]
print(findIndexOfZero(arr))
