class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u - 1, v - 1, w])  # Convert to zero-indexed

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        if rank[x] > rank[y]:
            parent[y] = x
        elif rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.v)]
        rank = [0] * self.v

        while e < self.v - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)

        for u, v, weight in result:
            print(f"{u + 1}-{v + 1}: {weight}")  # Convert back to one-indexed for output


if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    edges = int(input("Enter the number of edges: "))
    print("Enter each edge with its weight:")

    for _ in range(edges):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    g.kruskal_algo()

#Time Complexity:O(ElogV)
#Space Complexity:O(E+V)
