n = int(raw_input("Enter total number of users: "))

matrix = [[0] * n for _ in range(n)]
adj_list = [[] for _ in range(n)]

m = int(raw_input("Enter number of connections: "))

for i in range(m):
    u, v = map(int, raw_input("Enter connection (u v): ").split())

    if u < 1 or u > n or v < 1 or v > n:
        print "Invalid user number!"
        continue

    matrix[u-1][v-1] = 1
    matrix[v-1][u-1] = 1

    adj_list[u-1].append(v)
    adj_list[v-1].append(u)

print "\nAdjacency Matrix:"
for row in matrix:
    print row

print "\nAdjacency List:"
for i in range(n):
    print i + 1, ":", adj_list[i]

print "\nGraph Representation:"
for i in range(n):
    print "User", i + 1, "->",
    for j in adj_list[i]:
        print j,
    print

u, v = map(int, raw_input("\nEnter two users to check connection: ").split())

if u < 1 or u > n or v < 1 or v > n:
    print "Invalid user number!"
else:
    if matrix[u-1][v-1] == 1:
        print "Using Adjacency Matrix: Users are directly connected."
    else:
        print "Using Adjacency Matrix: Users are not directly connected."

    if v in adj_list[u-1]:
        print "Using Adjacency List: Users are directly connected."
    else:
        print "Using Adjacency List: Users are not directly connected."
