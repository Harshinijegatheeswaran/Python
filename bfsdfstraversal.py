from collections import deque

n = int(raw_input("Enter the number of users: "))

graph = {}

print("\nEnter the user names:")
for i in range(n):
    user = raw_input("User %d: " % (i + 1))
    graph[user] = []

m = int(raw_input("\nEnter the number of friendships: "))

print("\nEnter friendships (User1 User2):")

for i in range(m):
    u, v = raw_input("Friendship %d: " % (i + 1)).split()

    if u in graph and v in graph:
        graph[u].append(v)
        graph[v].append(u)
    else:
        print("Invalid user name!")

def display_friends(user):
    print("\nDirect friends of %s:" % user)

    for friend in graph[user]:
        print(friend)

def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("\nBFS Traversal:")

    while queue:
        user = queue.popleft()
        print(user),

        for friend in graph[user]:
            if friend not in visited:
                visited.add(friend)
                queue.append(friend)

    print()

def dfs(start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start),

    for friend in graph[start]:
        if friend not in visited:
            dfs(friend, visited)

print("\nSocial Network:")

for user in graph:
    print(user, "->", graph[user])

start = raw_input("\nEnter the user to start traversal: ")

if start in graph:
    display_friends(start)

    bfs(start)

    print("\nDFS Traversal:")
    dfs(start)
    print()

else:
    print("User not found!")
