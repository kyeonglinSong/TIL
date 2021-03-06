 200802(일)

# DFS

### 1) DFS의 특징

- 모든 노드를 탐색하는 경우 사용하기 좋음.
- (상대적으로) 로직이 간단하지만 느리다.
- 트리 순회는 모두 DFS의 한 종류이다.
  - 전위 순회(1,2,3) | 중위 순회(2,1,3) | 후위 순회(2,3,1)



- 재귀 알고리즘의 형태
  - 더 이상 갈 길이 없으면 (모든 노드를 탐색) 앞 노드로 백트래킹한다.
- 노드의 방문여부를 검사해야 한다. 그렇지 않으면 무한루프에 빠질수도.



- 경우의 수를 재귀함수로 모두 확인하기.



### 2) DFS 구현

- 재귀함수를 사용해서 구현한다.
- 배열로 구현한 그래프의 DFS 시간복잡도 : O(n^2)
- 벡터(인접리스트)로 구현한 그래프의 DFS 시간복잡도 : O(|E|+|V|)



- 벡터로 구현할 경우 `vector<pair<type,type>>`을 이용한다.

  

1. 노드 방문
2. 현재 노드와 인접한 정점을 모두 탐색
3. 만약 탐색하지 않은 노드가 있다면 그 노드로 재귀함수 호출



### 3) 관련 문제

- 기본적인 그래프 탐색 문제
- BF 관련 문제. 방문하거나 안하거나 (ex. 부분집합)
- 이차원 DFS 문제
- 최소비용 문제 : 가중치를 최소화



