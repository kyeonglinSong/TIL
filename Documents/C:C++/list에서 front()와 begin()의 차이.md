190926(목)

## C++ STL List 



### 1. STL list에서 front()와 begin()의 차이

- begin() 은 반복자의 첫번째 위치를 가리킨다.
- front() 은 첫번째 데이터의 레퍼런스를 반환해준다.





### 2. 연결리스트에서 반복자

``` c++
list<type>::iterator it;

it = arr.erase(it);

```

- 삭제할 때  iterator 안에도 넣어줘야지 삭제된거 반영된다.
- itreator가 가리키는 원소를 삭제하면 it는 그 다음 원소를 가리키게 된다.



