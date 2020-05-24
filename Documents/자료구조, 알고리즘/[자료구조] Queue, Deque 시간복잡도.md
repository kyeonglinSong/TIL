# [자료구조] Queue, Deque 시간복잡도



### 1. queue

front와 rear이 존재한다. 

- empty() : O(1)
  - front 확인하면 됨
- size() : O(1)
  - rear - front = size
- enqueue (push) : O(1)
- dequeue (pop) : O(1)





### 2. dequeue

- 앞뒤로 push pop이 가능한 큐.
- 시간복잡도 O(1)로 push, pop이 가능하다
- 그러나 공간을 많이 잡아먹음.