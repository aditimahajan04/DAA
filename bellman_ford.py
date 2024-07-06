class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        # Add an edge to the graph with a weight
        self.edges.append((u, v, w))

    def bellman_ford(self, src):
        # Initialize distances from source to all other vertices as infinite
        distances = [float('inf')] * self.vertices
        distances[src] = 0  # Distance to source itself is 0

        # Relax all edges |V| - 1 times
        for i in range(self.vertices - 1):
            for u, v, w in self.edges:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        # Check for negative-weight cycles
        for u, v, w in self.edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                print("Graph contains negative weight cycle")
                return None

        return distances


# Create a graph with 6 vertices
g = Graph(6)
# Add edges with weights
g.add_edge(0, 1, 6)  # Edge a -> b
g.add_edge(0, 2, -4)  # Edge a -> c
g.add_edge(0, 3, -3)  # Edge a -> d
g.add_edge(1, 4, 4)  # Edge b -> t
g.add_edge(2, 4, 3)  # Edge c -> t
g.add_edge(3, 1, -1)  # Edge d -> b
g.add_edge(3, 4, 4)  # Edge d -> t
g.add_edge(3, 2, -2)  # Edge d -> c
g.add_edge(4, 5, 2)  # Edge t -> e
g.add_edge(2, 5, 8)  # Edge c -> e
g.add_edge(3, 5, -3)  # Edge d -> e

# Run Bellman-Ford algorithm from vertex 0 (assuming 'a' is vertex 0)
result = g.bellman_ford(0)
if result:
    print("Vertex Distance from Source")
    for i in range(len(result)):
        print(f"{i}\t\t{result[i]}")
