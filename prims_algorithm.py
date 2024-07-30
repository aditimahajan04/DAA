import heapq
INF = 999999
V = 5
G = [
    [0,4,0,5,0],
    [4,0,3,1,0],
    [0,3,0,7,8],
    [5,1,7,0,3],
    [0,0,8,3,0]
]
def prim(graph, V):
    selected = [False] * V
    min_heap = []
    mst_edges = []

    selected[0] = True
    for j in range(V):
        if graph[0][j] != 0:
            heapq.heappush(min_heap, (graph[0][j], 0, j))  # Corrected: added missing parentheses

    while len(mst_edges) < V - 1:
        weight, u, v = heapq.heappop(min_heap)
        if selected[v]:
            continue

        selected[v] = True
        mst_edges.append((u, v, weight))

        for j in range(V):
            if not selected[j] and graph[v][j] != 0:
                heapq.heappush(min_heap, (graph[v][j], v, j))

    print("Edge: Weight")
    for u, v, weight in mst_edges:
        print(f"{u}-{v}: {weight}")

prim(G, V)


