
'''
bfs dfs 는 스택과 큐로 만듬.
이때 한번 들어간 노드는 다시 들어가지못함.
즉, 노드가 스택과 큐에 들어갔던 적이 있는지 확인이 필요.


'''

N,M,V = map(int,input().split())

#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1


#N이 3이면, visitied1 = [0, 0, 0, 0]
visited = [0]*(N+1)
visited2 = visited.copy()


#재귀를 이용해서 dfs함수 만들기
def dfs(V):
    visited[V] = 1 # 기본 0에서 방문했으니 1
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(V):
    queue = [V]
    visited2[V] = 1
    while queue:
        V = queue.pop(0)
        for i in range(1, N+1):
            if(visited2[i] == 0 and graph[V][i] ==1):
                queue.append(i)
                visited2[i]