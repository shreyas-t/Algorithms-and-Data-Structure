# Problem: Find Min no of Plaforms given Trains Arrival and Departure Time

def findPlatform(arr, dep, n):
    
    arr.sort()
    dep.sort()
    
    i = 0
    j = 0
    platform = 0
    count = 0

    while i < n and j < n:
        
        if arr[i] < dep [j]:
            i +=1
            count += 1 
            platform = max(platform, count)
        else:
            j +=1
            count -= 1
    
    return platform

arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 
n = len(arr) 
  
print("Minimum Number of Platforms Required = ", findPlatform(arr, dep, n)) 