# https://www.techiedelight.com/print-sub-arrays-array-distinct-elements/

from collections import defaultdict

def printDistinctSubArray(arr):
    n = len(arr)

    mp = defaultdict(bool)
    start = 0
    end = 0

    while end<n:

        while end < n and not mp[arr[end]]:
            mp[arr[end]] = True
            end += 1

        print(arr[start:end])

        while end < n and  mp[arr[end]]:
            mp[arr[start]] = False
            start += 1


arr = [5, 2, 3, 5, 4, 3]
printDistinctSubArray(arr)
