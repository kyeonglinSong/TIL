# [C++ STL] unordered_map



### unordered_map

python의 dictionary, java의 hash테이블인가 맵인가.. 아무튼. 그냥 해시맵이다.

  C++에서 unordered_map은 hash table로 구현된다.



### 초기화

```c++
unordered_map<key_type, value_type> map;
```



### 삽입 / 삭제

```c++
// 삽입
map[key] = value;

// 삭제
map.erase(key);
```



### 원소 접근

iterator를 사용하여 접근한다.

key와 value에 접근할 때 ->를 사용하는데, first는 key, second는 value 이다.

```c++
unordered_map<type, type>:: iterator iter;

for(iter=map.begin() ; iter!=map.end() ; iter++)
  	iter->first // key
  	iter->second // value
```

