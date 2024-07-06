from collections import defaultdict

class Graph:
    def __init__(self, num_nodes):
        # Initialize the graph using a dictionary of lists
        self.graph = defaultdict(list)
        # Store the number of nodes in the graph
        self.num_nodes = num_nodes

    def addEdge(self, u, v):
        # Add an edge from node u to node v
        self.graph[u].append(v)

    def BFS(self, s):
        # Initialize all nodes as not visited
        visited = [False] * (self.num_nodes + 1)
        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Loop until the queue is empty
        while queue:
            # Dequeue a node from the queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent nodes of the dequeued node
            # If an adjacent node has not been visited, mark it as visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

if __name__ == '__main__':
    # Define the number of nodes in the graph
    num_nodes = 5
    # Create a graph object
    g = Graph(num_nodes)
    # Add edges to the graph
    g.addEdge(1, 4)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(4, 3)

    # Perform BFS traversal starting from node 1
    print("BFS Traversal starting from node 1:")
    g.BFS(1)
