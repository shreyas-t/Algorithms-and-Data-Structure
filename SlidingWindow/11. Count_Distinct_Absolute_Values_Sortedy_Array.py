# https://www.techiedelight.com/count-distinct-absolute-values-sorted-array/

def findDistinct(arr):
    n = len(arr)

    start = 0
    end = n-1

    distinct = n

    while start < end:

        while start < end and arr[start] == arr[start+1]:
            start += 1
            distinct -= 1

        while start < end and arr[end] == arr[end-1]:
            end -= 1
            distinct -= 1
        
        if start == end:
            break

        sum = arr[start] + arr[end]    
        
        if sum == 0:
            distinct -= 1
            start += 1
            end -= 1

        elif sum<0:
            start += 1
        
        else:
            end -= 1

    return distinct  

arr = [-1, -1, 0, 1, 1, 1]
print(findDistinct(arr))