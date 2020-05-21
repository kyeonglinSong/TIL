200521(목)

# [C++] set

- 중복을 허용하지 않는 자료구조. python의 set과 같은 개념

- iterator로 접근한다.



```c++
set<type> st;
set<type>::iterator iter;

// 삽입
st.insert(something);
// 삭제
st.erase(시작인덱스, 끝인덱스);

//원소 접근
for(iter=st.begin() ; iter!=st.end() ; iter++)
{
  cout << iter;
}
```

