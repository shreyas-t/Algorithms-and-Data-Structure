from queue import Queue

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def maxHeight(root):

    if root is None:
        return 0

    q = Queue()
    q.put(root)

    height = 0

    while not q.empty():
        count = q.qsize()
        height += 1

        while count > 0:
            node = q.get()
            count -= 1

            if node.left:
                q.put(node.left)
            
            if node.right:
                q.put(node.right)        
    
    return height

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
  
print ("Height of tree is %d" %(maxHeight(root))) 