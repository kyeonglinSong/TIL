191201(일)

# DFS

### 깊이 우선 탐색(Depth-First Search)

그래프의 모든 정점을 방문하는 가장 단순하고 고전적인 방법.

현재 정점과 인접한 간선들을 하나씩 검사하다가 아직 방문하지 않은 정점으로 향하는 간선이 있다면, 그 간선을 무조건 따라가는 방법이다. 이 과정에서 더이상 갈 곳이 없는 정점에 도달하면 뒤로 돌아간다.



```c++
vector<vector<int>> adj;
vector<bool> visited;

// dfs 알고리즘
void dfs(int here) 
{
  visited[here] = true;
  for(int i=0 ; i<adj[here].size() ; i++)
  {
    int there = adj[here][i];
    if(!visited[there])
      dfs[there];
  }
}

// 모든 정점을 방문
void dfsAll()
{
  visited = vector<bool>(adj.size(), false);
  for(int i=0 ; i<adj.size() ; i++)
    if(!visited[i])
      dfs[i];
}
```

그래프의 모든 정점들이 간선을 통해 연결되어 있다는 보장이 없기 때문에 `dfs()` 만으로는 모든 정점을 발견할 수 없다. 따라서 모든 정점에 대해 순서대로 `dfs()`를 호출하는 `dfsAll()` 함수가 존재한다.



#### DFS의 시간 복잡도

`dfs()`는 한 정점마다 한 번씩 호출되므로 |V|번 호출된다. 모든 정점에 대해 `dfs()`를 수행하고 나면 모든 간선을 한 번 혹은 두 번 확인한다. 따라서 **DFS의 시간복잡도는 O(|V|+|E|)** 이다.



#### DFS 활용

##### 1. 두 정점이 서로 연결되어 있는지 확인

`dfs()`를 수행한 후 visited[]를 참조하면 된다.



##### 2. 연결된 부분집합의 개수 세기

`dfs()` 함수는 시작한 정점에서 갈 수 있는 모든 정점을 방문하므로 `dfsAll()`에서 `dfs()`가 호출되는 횟수를 카운트하면 된다.



##### 3. 위상 정렬

위상 정렬은 의존성이 있는 작업들이 주어질 때, 이들을 어떤 순서로 수행해야 하는지 계산해준다. (B를 하기 위해서 A가 선행되어야 할 때, B는 A에 의존한다고 한다.)



