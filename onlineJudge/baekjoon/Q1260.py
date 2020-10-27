from collections import deque


def bfs(graph, s, visited):
    queue = deque([s])
    visited[s] = 1
    while queue:
        t = queue.popleft()
        print(t, end=" ")

        for i in sorted(graph[t]):
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


def dfs(graph, s, visited):
    visited[s] = 1
    print(s, end=" ")
    for i in sorted(graph[s]):
        if not visited[i]:
            dfs(graph, i, visited)


n, m, v = map(int, input().split(" "))
graph = [ []for _ in range(n+1) ] # 0번은 사용하지 않음

for i in range(m):
    temp = list(map(int, input().split(" ")))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

visited_d = [0] * (n+1)
visited_b = [0] * (n+1)

dfs(graph, v, visited_d)
print()
bfs(graph, v, visited_b)