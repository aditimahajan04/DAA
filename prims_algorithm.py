import heapq

def prim(graph, V):
    selected = [False] * V
    min_heap = []
    distances = [float('inf')] * V

    # Start from vertex 0 (assuming 0-indexed graph)
    selected[0] = True
    distances[0] = 0

    for j in range(V):
        if graph[0][j] != 0:
            heapq.heappush(min_heap, (graph[0][j], j))
            distances[j] = graph[0][j]

    while min_heap:
        weight, v = heapq.heappop(min_heap)
        if selected[v]:
            continue

        selected[v] = True
        for j in range(V):
            if not selected[j] and graph[v][j] != 0 and graph[v][j] < distances[j]:
                distances[j] = graph[v][j]
                heapq.heappush(min_heap, (graph[v][j], j))

    return distances

if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    G = [[0 for _ in range(V)] for _ in range(V)]

    print("Enter each edge with weight (format: u v weight):")
    for _ in range(E):
        u, v, weight = map(int, input().split())
        G[u - 1][v - 1] = weight
        G[v - 1][u - 1] = weight

    distances = prim(G, V)
    print("Shortest distances from source vertex:")
    print(" ".join(map(str, distances)))

#Time Complexity: O(ElogV)
#Space Complexity: O(V^2)
