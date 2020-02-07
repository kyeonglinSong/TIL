# [python] stack, queue

알고리즘 풀이를 위한 파이썬!

### 1. stack

파이썬에서 스택은 별도의 설정 없이 그냥 리스트에서 쓸 수 있다. 와우!

```python
stack.pop()
stack.push("something")
#스택이 비어있으면 while문 탈출
while stack:
```



### 2. queue

`import queue, q = queue.Queue()`

라는 모듈이 있지만, 그냥 list를 큐처럼 사용할 수 있다.

```python
q.pop(0) #맨 먼저 들어온 요소 삭제
q.append() #뒤에 요소 삽입
```

