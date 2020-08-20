200820(목)

# [알고리즘] 다이나믹 프로그래밍 Top-Down, Bottom-Up

### Top-Down

- 재귀 호출 이용
- DFS 형태

- 아래에서부터 쌓아올리는 형태

```c++
dp(next, term+next_term);
```



### Bottom-Up

- 아래에서부터 쌓아올리는 형태

```c++
dp[i] = dp[i-1] + dp[i+1];
```

