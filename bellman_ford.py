class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []  # Initialize an empty list to store edges

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))  # Add an edge from vertex u to vertex v with weight w

    def bellman_ford(self, src):
        # Initialize distances from source to all vertices as infinite
        distances = [float('inf')] * self.vertices
        distances[src] = 0  # Distance to source itself is 0

        # Relax all edges |V| - 1 times
        for i in range(self.vertices - 1):
            for u, v, w in self.edges:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w  # Update distance if a shorter path is found

        # Check for negative-weight cycles
        for u, v, w in self.edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                print("Graph contains negative weight cycle")
                return None

        return distances  # Return the list of distances from the source to each vertex


# Create a graph with 6 vertices
g = Graph(6)
# Add edges with respective weights
g.add_edge(0, 1, -4)
g.add_edge(0, 5, -3)
g.add_edge(1, 3, -1)
g.add_edge(1, 4, -2)
g.add_edge(2, 1, 8)
g.add_edge(2, 5, 3)
g.add_edge(3, 0, 6)
g.add_edge(3, 5, 4)
g.add_edge(4, 2,-3)
g.add_edge(4, 5, 2)

# Run Bellman-Ford algorithm from vertex 0
result = g.bellman_ford(0)
if result:
    print("Vertex Distance from Source")
    for i in range(len(result)):
        print(f"{i}\t\t{result[i]}")


#Time complexity:O(V*E)
#Space complexity:O(V+E)
