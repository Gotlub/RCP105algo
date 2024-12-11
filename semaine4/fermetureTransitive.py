def transitive_closure(graph):
    V = len(graph)
    closure = [[0] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            closure[i][j] = graph[i][j]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])
    return closure
graph = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0]
]
graph2 = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 0, 0]
]

result = transitive_closure(graph2)
print("Transitive Closure:")
for row in result:
    print(row)
