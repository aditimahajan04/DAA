import heapq

class Solution:
    def dijkstra(self, v, adj, s):
        # Initialize a priority queue
        pq = []
        # Initialize distances to all vertices as infinite
        distTo = [float('inf')] * v
        # Distance to the source is 0
        distTo[s] = 0

        # Push the source node into the priority queue with distance 0
        heapq.heappush(pq, (0, s))

        while pq:
            # Pop the vertex with the smallest distance
            dis, node = heapq.heappop(pq)
            # Traverse all the adjacent vertices of the popped vertex
            for neighbour in adj[node]:
                v, w = neighbour
                # If the distance to the neighbour is shorter through the current node
                if dis + w < distTo[v]:
                    # Update the distance to the neighbour
                    distTo[v] = dis + w
                    # Push the updated distance to the priority queue
                    heapq.heappush(pq, (dis + w, v))
        return distTo

if __name__ == "__main__":
    v = 6  # Number of vertices in the graph
    s = 1  # Source vertex
    # Initialize the adjacency list
    adj = [[] for _ in range(v)]

    # Add edges to the adjacency list (u -> v with weight w)
    adj[1].append([2, 10])
    adj[1].append([5, 100])
    adj[2].append([3, 50])
    adj[3].append([4, 20])
    adj[3].append([5, 10])
    adj[4].append([5, 60])

    # Create a Solution object
    solution = Solution()
    # Get the shortest paths from the source vertex
    res = solution.dijkstra(v, adj, s)

    # Print the shortest distance to all vertices
    for distance in res:
        print(distance, end=" ")
    print()
