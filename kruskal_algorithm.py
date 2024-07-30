class Graph:
    def __init__(self,vertices):
        self.v=vertices;
        self.graph=[]
    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])
    def find(self,parent,i):
        if parent[i]==i:
            return i
        return self.find(parent,parent[i])
    def apply_union(self,parent,rank,x,y):
        if rank[x]>rank[y]:
            parent[x]=y
        elif rank[x]<rank[y]:
            parent[y]=x
        else:
            parent[y]=x
            rank[x]+=1
    def kruskal_algo(self):
        result=[]
        i,e=0,0
        self.graph=sorted(self.graph,key=lambda item:item[2])
        parent=[i for i in range(self.v)]
        rank=[0]*self.v

        while e<self.v-1:
            u,v,w=self.graph[i]
            i+=1
            x=self.find(parent,u)
            y=self.find(parent,v)
            if x!=y:
                e+=1
                result.append([u,v,w])
                self.apply_union(parent,rank,x,y)

        for u,v,weight in result:
            print("%d-%d:%d" %(u,v,weight))

g=Graph(5)
g.add_edge(0,1,10)
g.add_edge(0,4,5)
g.add_edge(4,3,5)
g.add_edge(3,2,2)
g.add_edge(2,1,1)
g.add_edge(4,1,6)
g.add_edge(4,2,7)
g.kruskal_algo()
