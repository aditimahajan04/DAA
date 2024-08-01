import heapq
class Solution:
    def dijkstra(self, v, adj, s):
        pq = []
        distTo = [float('inf')] * v
        distTo[s] = 0

        heapq.heappush(pq, (0, s))

        while pq:
            dis, node = heapq.heappop(pq)
            for neighbour in adj[node]:
                v, w = neighbour
                if dis + w < distTo[v]:
                    distTo[v] = dis + w
                    heapq.heappush(pq, (dis + w, v))
        return distTo


if __name__ == "__main__":
    # Read number of vertices
    v = int(input("Enter the number of vertices: "))

    # Read number of edges
    e = int(input("Enter the number of edges: "))

    # Initialize adjacency list
    adj = [[] for _ in range(v)]

    print("Enter each edge with its weight in the format 'start end weight':")
    for _ in range(e):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))  # Add edge u -> v with weight w

    # Read the source vertex
    s = int(input("Enter the source vertex: "))

    solution = Solution()
    res = solution.dijkstra(v, adj, s)

    print("Shortest distances from source vertex:")
    for distance in res:
        print(distance, end=" ")
    print()

#Time Complexity: O((V+E)logV)
#Space Complexity: O(V+E)
