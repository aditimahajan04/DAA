from collections import defaultdict

class Graph:
    def __init__(self, num_nodes):
        # Initialize the graph with the given number of nodes
        self.graph = defaultdict(list)  # Use defaultdict to handle adjacency list
        self.num_nodes = num_nodes  # Store the number of nodes in the graph

    def addEdge(self, u, v):
        # Add an edge from node u to node v
        self.graph[u].append(v)

    def BFS(self, s):
        # Perform BFS starting from node s
        visited = [False] * (self.num_nodes + 1)  # Keep track of visited nodes
        queue = []  # Initialize the queue for BFS

        # Start BFS from the source node s
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)  # Dequeue a node from the front of the queue
            print(s, end=" ")  # Print the node

            # Process all adjacent nodes
            for i in self.graph[s]:
                if not visited[i]:  # If the adjacent node has not been visited
                    queue.append(i)  # Enqueue the node
                    visited[i] = True  # Mark the node as visited

if __name__ == '__main__':
    # Read the number of nodes from the user
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    g = Graph(num_nodes)  # Create a graph instance with the given number of nodes

    # Read the number of edges from the user
    num_edges = int(input("Enter the number of edges: "))

    print("Enter the edges in the format 'u v':")
    # Read each edge from the user and add it to the graph
    for _ in range(num_edges):
        u, v = map(int, input().split())  # Read the edge as two integers
        g.addEdge(u, v)  # Add the edge to the graph

    # Read the starting node for BFS traversal
    start_node = int(input("Enter the starting node for BFS traversal: "))

    # Perform BFS starting from the specified node
    print("BFS Traversal starting from node", start_node, ":")
    g.BFS(start_node)

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
