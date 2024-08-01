import heapq


def prim(graph, V):
    selected = [False] * V
    min_heap = []
    mst_edges = []

    selected[0] = True
    for j in range(V):
        if graph[0][j] != 0:
            heapq.heappush(min_heap, (graph[0][j], 0, j))

    while len(mst_edges) < V - 1:
        weight, u, v = heapq.heappop(min_heap)
        if selected[v]:
            continue

        selected[v] = True
        mst_edges.append((u, v, weight))

        for j in range(V):
            if not selected[j] and graph[v][j] != 0:
                heapq.heappush(min_heap, (graph[v][j], v, j))

    print("Minimum Spanning Tree (MST) edges:")
    print(" ".join([f"{u + 1}-{v + 1}: {weight}" for u, v, weight in mst_edges]))


if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))

    # Initialize the adjacency matrix
    graph = [[0] * V for _ in range(V)]

    edges = int(input("Enter the number of edges: "))
    print("Enter each edge with its weight (u v w):")

    for _ in range(edges):
        u, v, w = map(int, input().split())
        graph[u - 1][v - 1] = w
        graph[v - 1][u - 1] = w  # Because the graph is undirected

    prim(graph, V)

#Time Complexity: O((V+E)logV)
#Space Complexity: O(V^2+E)
