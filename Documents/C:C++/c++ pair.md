191003(목)

## C++ pair 사용법 

### 1. Pair 사용법

- 자료형 두 개를 묶을 수 있다.
- .first, .second로 접근한다.
- pair 안 pair도 가능!



- 알고리즘 문제 풀 때 vector<pair<type, type>> 으로 자주 사용하는듯.

```c++
pair<int, int> p;
p = make_pair(10, 20);
cout << p.first << p.second <<endl;   // 10, 20 출력
```





### 2. 비트연산자 >>, <<

```c++
a >> b  //a의 비트를 b만큼 오른쪽으로 이동
a << b  //a의 비트를 b만큼 왼쪽으로 이동
```