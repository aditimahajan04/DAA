from collections import defaultdict

class Graph:
    def __init__(self):
        # Initialize the graph using a default dictionary where each key has a list as its default value.
        # This will store the adjacency list of the graph.
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        # Add an edge from vertex 'u' to vertex 'v'.
        # This adds 'v' to the adjacency list of 'u'.
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        # A utility function for the DFS traversal.
        # It visits nodes recursively.

        # Mark the current node as visited.
        visited.add(v)

        # Print the visited node.
        print(v, end=" ")

        # Recur for all the vertices adjacent to this vertex.
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                # If a neighbouring node hasn't been visited, recursively visit it.
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        # The main function that initializes the DFS traversal.

        # Create a set to store visited vertices.
        visited = set()

        # Call the DFS utility function starting from the given vertex 'v'.
        self.DFSUtil(v, visited)


# Driver code to test the above implementation
if __name__ == "__main__":
    g = Graph()  # Create a graph object

    # Take user input for the number of edges
    num_edges = int(input("Enter the number of edges: "))

    # Take user input for each edge
    print("Enter each edge as a pair of space-separated vertices (u v):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        g.addEdge(u, v)

    # Take user input for the starting vertex for DFS
    start_vertex = int(input("Enter the starting vertex for DFS: "))

    # Print the DFS traversal starting from the user-specified vertex
    print("DFS starting from vertex", start_vertex, ":")
    g.DFS(start_vertex)

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
