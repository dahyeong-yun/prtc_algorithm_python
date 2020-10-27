def dfs(graph, v, visited):
    visited[v] = 1
    # print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


n = int(input()) # 컴퓨터의 수 n <= 100
linked = int(input()) # 연결되어 있는 컴퓨터의 수

graph = [ set([]) for _ in range(n+1) ] # 0번은 사용하지 않음

for i in range(linked):
    temp = list(map(int, input().split(" ")))
    graph[temp[0]].add(temp[1])
    graph[temp[1]].add(temp[0])


visited = [0] * (n+1)

dfs(graph, 1, visited)

print(sum(visited)-1)