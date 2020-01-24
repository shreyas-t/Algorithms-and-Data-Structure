# Activity Selection using Greedy Algorithm

class Activity:
    
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish


def printMaxActivities(arr):

    arr = sorted(arr,key =  lambda a: a.finish)
    i = 0

    print(arr[i].start, arr[i].finish)

    for j in range(1,len(arr)):
        if arr[j].start >= arr[i].finish:
            print(arr[j].start, arr[j].finish)
            i = j


list = []

list.append(Activity(5, 9))
list.append(Activity(1, 2))
list.append(Activity(3, 4))
list.append(Activity(0, 6))
list.append(Activity(5, 7))
list.append(Activity(8, 9))

printMaxActivities(list)










