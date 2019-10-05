191005(토)
# c++ vector subscript out of range 오류



```c++
int n;
vector<int> arr(n); 

for(int i=1 ; i<=n ; i++)
    ...
```

이런식으로 코드를 짜다 보면 가끔 vector subscript out of range 오류가 뜬다.



- 이유 : null값인 인덱스가 존재..
- dp 문제를 풀 때 편의상 0~n-1이 아니라 1~n으로 접근할 때 arr[0]이 초기화 되어있지 않으면 오류가 생긴다.

