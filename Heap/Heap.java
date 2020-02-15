import java.util.*;

abstract class Heap{
    protected int capacity;
    protected int size;
    protected int items[];

    public Heap(){
        this.capacity = 10;
        this.size = 0;
        this.items = new int[this.capacity];
    }

    public int getLeftChildIndex(int parentIndex){
        return 2*parentIndex + 1;
    }

    public int getRightChildIndex(int parentIndex){
        return 2*parentIndex + 2;
    }

    public int getParentIndex(int childIndex){
        return (childIndex-1)/2;
    }

    public boolean hasLeftChild(int index){
        return getLeftChildIndex(index) < size;
    }

    public boolean hasRightChild(int index){
        return getRightChildIndex(index) < size;
    }

    public boolean hasParent(int index){
        return getLeftChildIndex(index) >= 0;
    }
    
    public int leftChild(int index){
        return items[getLeftChildIndex(index)];
    }

    public int rightChild(int index){
        return items[getRightChildIndex(index)];
    }

    public int parent(int index){
        return items[getParentIndex(index)];
    }

    public void swap(int indexOne, int indexTwo){
        int temp = items[indexOne];
        items[indexOne] = items[indexTwo];
        items[indexTwo] = temp;
    }

    public void isEmpty(String methodname){
        if(size == 0){
            throw new IllegalStateException("You cannot perform '" + methodname + "' on an empty heap");
        }
    }   

    public int peek(){
        isEmpty("peek");
        return items[0];
    }

    public void ensureCapacity(){
        if(size == capacity){
            capacity = capacity << 1;
            items = Arrays.copyOf(items, capacity);
        }
    }

    public void add(int item){
        ensureCapacity();
        items[size] = item;
        size++;
        heapifyUp();
    }

    public int poll(){
        isEmpty("poll");
        int item = items[size-1];
        size--;
        heapifyDown();
        return item;
    }
    
    public abstract void heapifyUp();
    public abstract void heapifyDown();
}

class MaxHeap extends Heap{

    public void heapifyUp(){
        int index = size-1;
        
        while(hasParent(index) && parent(index)< items[index]){
            swap(getParentIndex(index), index);
            index = getParentIndex(index);
        }
    }

    public void heapifyDown(){
        int index = 0;

        while(hasLeftChild(index)){
            int smallerChildIndex = getLeftChildIndex(index);

            if(hasRightChild(index) && rightChild(index) > leftChild(index)){
                smallerChildIndex = getRightChildIndex(index);
            }
            if(items[index] > items[smallerChildIndex]){
                break;
            }
            swap(smallerChildIndex, index);
            index = smallerChildIndex;
        }

    }
}
class MinHeap extends Heap{

        public void heapifyUp(){
            int index = size-1;
            
            while(hasParent(index) && parent(index)> items[index]){
                swap(getParentIndex(index), index);
                index = getParentIndex(index);
            }
        }
    
        public void heapifyDown(){
            int index = 0;
    
            while(hasLeftChild(index)){
                int smallerChildIndex = getLeftChildIndex(index);
    
                if(hasRightChild(index) && rightChild(index) < leftChild(index)){
                    smallerChildIndex = getRightChildIndex(index);
                }
                if(items[index] < items[smallerChildIndex]){
                    break;
                }
                swap(smallerChildIndex, index);
                index = smallerChildIndex;
            }
    
        }
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            int range = scanner.nextInt();
            scanner.close();
            
            // Insert random values into heaps:
            Heap minHeap = new MinHeap();
            Heap maxHeap = new MaxHeap();
            System.out.println("Insert Number Sequence:");
            for(int i = 0; i < range; i++) {
                int value = (int) (Math.random() * 100);
                minHeap.add(value);
                maxHeap.add(value);
                System.out.print(+ value + " ");
            }
            
            // Remove values from heaps:
            System.out.println("\n\nPoll Values:\n------------\nMinHeap MaxHeap");
            for(int i = 0; i < range; i++) {
                System.out.format("  %-12d", minHeap.poll());
                System.out.format("%-6d\n", maxHeap.poll());
            }
            try {
                minHeap.peek();
            }
            catch(IllegalStateException e) {
                System.out.println(e.getMessage());
            }
            try {
                maxHeap.poll();
            }
            catch(IllegalStateException e) {
                System.out.println(e.getMessage());
            }
        }
    }
    
    


 