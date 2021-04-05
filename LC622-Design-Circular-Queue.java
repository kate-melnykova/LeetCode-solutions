/*
Design your implementation of the circular queue. The circular queue is a linear data
structure in which the operations are performed based on FIFO (First In First Out) principle
and the last position is connected back to the first position to make a circle. It is also
called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front
of the queue. In a normal queue, once the queue becomes full, we cannot insert the next
element even if there is a space in front of the queue. But using the circular queue, we
can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the
operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the
operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.


Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue",
"enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4


Constraints:
(*) 1 <= k <= 1000
(*) 0 <= value <= 1000
(*) At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

Follow up: Could you solve the problem without using the built-in queue?
*/
class MyCircularQueue {
    int[] queue;
    int queueLength;
    int head;
    int tail;
    boolean empty;

    public MyCircularQueue(int k) {
        // Time complexity: O(1)
        // Space complexity: O(k) -- need to create a new array
        this.queueLength = k;
        this.head = 0;
        this.tail = -1;
        this.queue = new int[k];
        this.empty = true;
    }

    public boolean enQueue(int value) {
        // Time complexity: O(1)
        // Space complexity: O(1)
        if (this.tail == -1){
            this.queue[0] = value;
            this.tail = 0;
            this.empty = false;
            return true;
        } else if (isFull()){
            return false;
        } else {
            if (this.tail == this.queueLength - 1){
                this.tail = 0;
            } else {
                this.tail++;
            }
            this.empty = false;
            this.queue[this.tail] = value;
            return true;
        }
    }

    public boolean deQueue() {
        // Time complexity: O(1)
        // Space complexity: O(1)
        if (isEmpty()){
            return false;
        } else {
            if (this.head == this.tail){
                this.empty = true;
            }
            if ((this.head == this.queueLength - 1)){
                this.head = 0;
            } else {
                this.head++;
            }
            return true;
        }
    }

    public int Front() {
        // Time complexity: O(1)
        // Space complexity: O(1)
        if (isEmpty()){
            return -1;
        } else {
            return this.queue[this.head];
        }
    }

    public int Rear() {
        // Time complexity: O(1)
        // Space complexity: O(1)
        if (isEmpty()){
            return -1;
        } else {
            return this.queue[this.tail];
        }
    }

    public boolean isEmpty() {
        // Time complexity: O(1)
        // Space complexity: O(1)
        return this.empty;
    }

    public boolean isFull() {
        // Time complexity: O(1)
        // Space complexity: O(1)
        if ((!this.empty) && ((this.tail + 1 == this.head) || ((this.head == 0) && (this.tail == this.queueLength - 1)))){
            return true;
        } else {
            return false;
        }
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */