class Graph:
    def __init__(self, vertices):
        """
        Initialize the graph with the given number of vertices.
        """
        self.vertices = vertices
        self.adj_list = [[] for _ in range(self.vertices)]  # Adjacency list for the graph
        self.visited = [False] * self.vertices  # Track visited vertices
        self.count = 0  # Count of visited vertices
        self.min_cost = float('inf')  # Initialize the minimum cost to infinity

    def add_edge(self, u, v, w):
        """
        Add an edge between vertices u and v with weight w.
        """
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))  # Since the graph is undirected

    def tsp(self, src, node, cost):
        """
        Solve the Traveling Salesman Problem using backtracking.

        Parameters:
        - src: the starting vertex
        - node: the current vertex
        - cost: the cost of the current path
        """
        if self.count == self.vertices and node == src:
            # All vertices are visited and we are back to the source
            self.min_cost = min(self.min_cost, cost)
        for v, w in self.adj_list[node]:
            if not self.visited[v]:
                self.visited[v] = True
                self.count += 1
                self.tsp(src, v, cost + w)
                # Backtrack
                self.visited[v] = False
                self.count -= 1


if __name__ == "__main__":
    # Input the number of vertices
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    # Input the number of edges
    edges = int(input("Enter the number of edges: "))
    print("Enter each edge with its vertices (u, v) and weight (w):")

    for _ in range(edges):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    # Start the TSP from vertex 0
    g.tsp(0, 0, 0)

    # Print the minimum cost of the TSP
    print("Minimum cost of the TSP:", g.min_cost)

#Time Complexity:O(n!)
#Space Complexity:O(n)
