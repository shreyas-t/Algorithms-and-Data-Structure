# https://www.techiedelight.com/count-distinct-elements-every-sub-array-size-k-array/

from collections import defaultdict 

def findDistinctCout(arr, k):
    n = len(arr)

    if k>n:
        return
    
    mp = defaultdict(int)
    distinct = 0

    for i in range(k):
        mp[arr[i]] += 1
        if(mp[arr[i]]==1):
            distinct += 1

    print("the count of distinct sub-array [{0}-{1}] is {2} ".format(0, k-1, distinct))
   

    for i in range(n-k):
        mp[arr[i]] -= 1
        mp[arr[i+k]] += 1

        if mp[arr[i+k]] == 1 :
            distinct += 1

        if mp[arr[i]] == 0:
            distinct -= 1
        
        print("the count of distinct sub-array [{0}-{1}] is {2} ".format(i+1, i+k, distinct))
        
        


arr = [2, 1, 2, 3, 2, 1, 4, 5]
findDistinctCout(arr, 5)