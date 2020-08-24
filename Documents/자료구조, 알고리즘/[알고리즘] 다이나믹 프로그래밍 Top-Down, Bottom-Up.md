200820(목)

# [알고리즘] 다이나믹 프로그래밍 Top-Down, Bottom-Up

### Top-Down

- 재귀 호출 이용
- DFS 형태

- 아래에서부터 쌓아올리는 형태
- 함수를 void형으로 만들고 바깥에 result 변수를 두면 편하다.

```c++
int result = 0; // OR MAX

void dp(something)
{
	dp(next, term+next_term);  
}

```



### Bottom-Up

- 아래에서부터 쌓아올리는 형태
- (중첩) for문과 조건문을 이용한다.
- 함수를 int형으로 만들고 for문이 끝나면 마지막 값(혹은 최대최소값)을 출력한다.

```c++
int dp(something)
{
	for()
    dp[i] = dp[i-1] + dp[i+1];
  
  return max // or something 
}

```

