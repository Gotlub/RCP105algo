from collections import defaultdict
 
# This class represents an directed graph
# using adjacency list representation
 
 
class Graph:
 
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
        self.Time = 0
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    '''A recursive function that find finds and prints strongly connected
    components using DFS traversal
    u --> The vertex to be visited next
    disc[] --> Stores discovery times of visited vertices
    low[] -- >> earliest visited vertex (the vertex with minimum
                discovery time) that can be reached from subtree
                rooted with current vertex
     st -- >> To store all the connected ancestors (could be part
           of SCC)
     stackMember[] --> bit/index array for faster check whether
                  a node is in stack
    '''
 
    def SCCUtil(self, u, low, disc, stackMember, st):
 
        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stackMember[u] = True
        st.append(u)
        #print(u,self.graph[u],low,disc,stackMember, st)
        # Go through all vertices adjacent to this
        for v in self.graph[u]:
            
            # If v is not visited yet, then recur for it
            if disc[v] == -1:
                self.SCCUtil(v, low, disc, stackMember, st)
 
                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                # Case 1 (per above discussion on Disc and Low value)
                low[u] = min(low[u], low[v])
 
            elif stackMember[v] == True:
 
                '''Update low value of 'u' only if 'v' is still in stack
                (i.e. it's a back edge, not cross edge).
                Case 2 (per above discussion on Disc and Low value) '''
                low[u] = min(low[u], disc[v])
        # head node found, pop the stack and print an SCC
        w = -1  # To store stack extracted vertices
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                print(w, end=" ")
                stackMember[w] = False
 
            print()
 
    # The function to do DFS traversal.
    # It uses recursive SCCUtil()
 
    def SCC(self):
 
        # Mark all the vertices as not visited
        # and Initialize parent and visited,
        # and ap(articulation point) arrays
        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stackMember = [False] * (self.V)
        st = []
 
        # Call the recursive helper function
        # to find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if disc[i] == -1:
                self.SCCUtil(i, low, disc, stackMember, st)
 
#a b c d e f g h i
#0 1 2 3 4 5 6 7 8
# Create a graph given in the above diagram
g1 = Graph(9)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(0, 4)
g1.addEdge(1, 5)
g1.addEdge(2, 3)
g1.addEdge(2, 7)
g1.addEdge(3, 8)
g1.addEdge(4, 5)
g1.addEdge(5, 6)
g1.addEdge(6, 4)
g1.addEdge(7, 6)
g1.addEdge(8, 7)
print("SSC in first graph ")
g1.SCC()
