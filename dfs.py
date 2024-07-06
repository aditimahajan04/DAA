from collections import defaultdict

class Graph:
    def __init__(self):
        # Initialize the graph using a dictionary of lists
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        # Add an edge from node u to node v
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=" ")

        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        # Create a set to store visited nodes
        visited = set()
        # Call the recursive helper function to perform DFS traversal
        self.DFSUtil(v, visited)

if __name__ == "__main__":
    # Create a graph object
    g = Graph()
    # Add edges to the graph
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 2)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(1, 4)

    # Perform DFS traversal starting from node 0
    print("DFS Traversal starting from node 0:")
    g.DFS(0)
