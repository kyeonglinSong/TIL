#[python] 알고리즘 풀때 유용한 문법

### 1. 문자열을 한글자씩 잘라서 리스트로

```python
string = "abcde"
list(string) #[a,b,c,d,e]
```



### 2. list1과 list2의 차집합

```python
list(set(list1)-set(list2))
```



### 3. n만큼 스트링 채우기

- str.rjust(n, 'char')

  