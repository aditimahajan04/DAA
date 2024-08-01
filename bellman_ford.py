class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices in the graph
        self.edges = []  # List to store edges as tuples (u, v, w)

    def add_edge(self, u, v, w):
        self.edges.append((u - 1, v - 1, w))  # Convert to zero-indexed

    def bellman_ford(self, src):
        # Initialize distances from source to all vertices as infinity
        distances = [float('inf')] * self.vertices
        distances[src] = 0  # Distance from source to itself is 0

        # Relax edges |V| - 1 times
        for i in range(self.vertices - 1):
            for u, v, w in self.edges:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        # Check for negative weight cycles
        for u, v, w in self.edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                print("Graph contains negative cycle")
                return None

        return distances


if __name__ == "__main__":
    # Input the number of vertices
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    # Input the number of edges
    edges = int(input("Enter the number of edges: "))
    print("Enter each edge with its weight (format: u v w):")

    for _ in range(edges):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    # Input the source vertex
    src = int(input("Enter the source vertex: ")) - 1  # Convert to zero-indexed

    # Run the Bellman-Ford algorithm
    result = g.bellman_ford(src)

    if result:
        print("Shortest distances from source vertex:")
        print(" ".join(map(str, result)))

# Time Complexity:O(V*E)
# Space Complexity:O(V+E)
