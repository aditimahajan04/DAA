# Travelling Salesman Problem using backtracking
class Graph:
    def __init__(self, vertices):
        # Initialize the graph with the number of vertices
        self.vertices = vertices
        # Adjacency list to store edges and weights
        self.adj_list = [[] for _ in range(self.vertices)]
        # List to keep track of visited vertices
        self.visited = [False] * self.vertices
        # Counter to count the number of visited vertices
        self.count = 0
        # Variable to store the minimum cost of the tour
        self.min_cost = float('inf')

    def add_edge(self, u, v, w):
        # Add an edge from vertex u to vertex v with weight w
        self.adj_list[u].append((v, w))
        # Since the graph is undirected, add an edge from v to u as well
        self.adj_list[v].append((u, w))

    def tsp(self, src, node, cost):
        # If all vertices are visited and we are back to the source
        if self.count == self.vertices and node == src:
            # Update the minimum cost if the current cost is less
            self.min_cost = min(self.min_cost, cost)
            return

        # Explore all adjacent vertices
        for v, w in self.adj_list[node]:
            if not self.visited[v]:
                # Mark the vertex as visited
                self.visited[v] = True
                # Increment the visited count
                self.count += 1
                # Recur for the next vertex
                self.tsp(src, v, cost + w)
                # Backtrack: unmark the vertex as visited
                self.visited[v] = False
                # Decrement the visited count
                self.count -= 1

if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = Graph(5)
    # Add edges with weights
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 12)
    g.add_edge(0, 4, 5)
    g.add_edge(1, 2, 4)
    g.add_edge(1, 3, 8)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 4, 3)
    g.add_edge(3, 4, 10)

    # Run the TSP algorithm starting from vertex 0
    g.tsp(0, 0, 0)
    # Print the minimum cost of the tour
    print(g.min_cost)
