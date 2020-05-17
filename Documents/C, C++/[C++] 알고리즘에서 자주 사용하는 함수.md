# 자주 사용하는 함수



###String 관련

- string -> int 

```c++
stoi()
```



- ASCII

대문자 A : 65

소문자 a : 97

대문자와 소문자 사이 간격은 32



- 공백 포함한 문자열 입력받기

scanf랑 cin은 공백을 기준으로 문자열을 가른다. 그러므로 공백을 포함한 문자열을 입력받으려면 gets()를 사용한다.

이때, 입력받는 문자열은 string type이 아니라 char[] type이어야 한다.



- 문자열 자르기

str.substr(시작범위, 끝범위)



- 문자열 대치

 str.replace(시작, 끝, 바꿀거);



- 문자열 뒤집기

replace(str.begin() , str.end())



### Stack & Queue

stack은 STL에 stack 이 따로 있다.

```c++
#include <stack>
stack<type> st;
```



queue는 queue가 따로 있지만 vector를 큐로 사용하면 된다.

```c++
#include <vector>
vector<type> queue;
```



priority queue는 따로 선언해야 한다.

```c++
#include <queue>
priority_queue<type> pq;
```





### math.h

- 제곱 : pow()