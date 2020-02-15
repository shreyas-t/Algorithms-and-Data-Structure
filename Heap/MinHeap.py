import math

class MinHeap:

    def __init__(self):
        self.heap = []
        self.size = 0

    def getParentIndex(self, i):
        return math.floor((i-1)/2)
    
    def getLeftChildIndex(self, i):
        return 2*i + 1
    
    def getRightChildIndex(self, i):
        return 2*i + 2
    
    def isEmpty(self, methodName):
        if not self.heap:
            raise Exception("You cannot perform '", methodName, "' on an empty heap")

    def parent(self, i):
        return self.heap[self.getParentIndex(i)]
    
    def leftChild(self, i):
        return self.heap[self.getLeftChildIndex(i)]
    
    def rightChild(self, i):
        return self.heap[self.getRightChildIndex(i)]
    
    def peek(self):
        self.isEmpty("peek")
        return self.heap[0]
    
    def hasParent(self, i):
        return self.getParentIndex(i) >= 0
    
    def hasLeftChild(self, i):
        return self.getLeftChildIndex(i) < self.size
    
    def hasRightChild(self, i):
        return self.getRightChildIndex(i) < self.size

    def heapifyUp(self):
        index = self.size - 1

        while self.hasParent(index) and self.parent(index) > self.heap[index]:
            self.heap[index], self.heap[self.getParentIndex(index)] =  self.heap[self.getParentIndex(index)], self.heap[index]
            index = self.getParentIndex(index)

    

    def heapifyDown(self):
        index = 0

        while self.hasLeftChild(index):
            smallestChildIndex = self.getLeftChildIndex(index)

            if self.hasRightChild(index) and self.rightChild(index) < self.heap[smallestChildIndex]:
                smallestChildIndex = self.getRightChildIndex(index)
            
            if self.heap[smallestChildIndex] > self.heap[index]:
                break

            self.heap[index], self.heap[smallestChildIndex] = self.heap[smallestChildIndex] , self.heap[index]

            index = smallestChildIndex
                       

    def add(self, item):
        self.heap.append(item)
        self.size += 1
        self.heapifyUp()
    
    def poll(self):
        self.isEmpty("poll")
        item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(0)
        self.size -= 1
        self.heapifyDown()
        return item

    def print(self):
        print(self.heap)

heapObj = MinHeap() 
heapObj.add(3) 
heapObj.add(2) 
heapObj.add(1) 
heapObj.add(15) 
heapObj.add(5) 
heapObj.add(4) 
heapObj.add(45) 
heapObj.print()
  
print(heapObj.poll(),)
heapObj.print()
