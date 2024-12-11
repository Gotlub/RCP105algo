# Floyd Warshall Algorithm in python


# The number of vertices

INF = 1e7


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j if j!=0 else INF, i)), G))
    nV = len(G)
    parent = [[k+1 for _ in range(len(G))] for k in range(len(G))]
    print(distance)
    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
              if( i!=j and distance[i][j] >  distance[i][k] + distance[k][j]):
                distance[i][j] =  distance[i][k] + distance[k][j]
                parent[i][j] = parent[k][j]
        print_solution(distance)
        print("parent")
        print_parent(parent)
        print()

# Printing the solution
def print_solution(distance):
    nV = len(distance)
    for i in range(nV):
        for j in range(nV):
            if(i == j):
                print(0, end=" ")
            elif(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

def print_parent(parent):
    nV = len(parent)
    for i in range(nV):
        for j in range(nV):
            print(parent[i][j], end="  ")
        print(" ")


G = [[0, 0, 3, 8],
     [5, 0, 0, 2],
     [4, 3, 0, 0],
     [0, 6, 0, 0],]
floyd_warshall(G)
