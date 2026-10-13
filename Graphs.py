n = int(raw_input("Enter number of cities: "))

print("Enter adjacency matrix (0 for no connection):")
graph = []

for i in range(n):
    row = list(map(int, raw_input().split()))
    graph.append(row)

source = int(raw_input("Enter source city (0 to n-1): "))
destination = int(raw_input("Enter destination city (0 to n-1): "))

dist = [float('inf')] * n
parent = [-1] * n
visited = [False] * n

dist[source] = 0

for _ in range(n):
    u = -1

    for i in range(n):
        if not visited[i] and (u == -1 or dist[i] < dist[u]):
            u = i

    if u == -1 or dist[u] == float('inf'):
        break

    visited[u] = True

    for v in range(n):
        if graph[u][v] > 0 and not visited[v]:
            new_dist = dist[u] + graph[u][v]

            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u

if dist[destination] == float('inf'):
    print("No path exists")
else:
    path = []
    v = destination

    while v != -1:
        path.append(v)
        v = parent[v]

    path.reverse()

    print("Shortest path:", " -> ".join(map(str, path)))
    print("Shortest distance:", dist[destination])
