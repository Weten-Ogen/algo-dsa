class Vertex:
    def __init__(self,n):
        self.name = n

class Graph:
    vertices = {}
    edges = []
    edge_indicies = {}

    def add_vertex(self, vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indicies[vertex.name] = len(self.edge_indicies)
            return True
        else:
            return False
        
    def add_edge(self, u , v, weight= 1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indicies[u]][self.edge_indicies[v]] = weight
            self.edges[self.edge_indicies[v]][self.edge_indicies[u]] = weight
            return True
        else:
            return False
    
    def print_graph(self):
        print()
        print(self.edges)
        print()
        print(self.edge_indicies)
        for v , i in sorted(self.edge_indicies.items()):
            print(v + ' ', end=" ")
            for j in range(len(self.edges)):
                print(self.edges[i][j], end = ' ')
            print(' ') 


g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'),ord('K')):
    g.add_vertex(Vertex(chr(i)))



edges = ['AB', 'AE','BF','CG', 'DE', 'DH','EH','FG','FI','FJ','GJ']
for edge in edges:
    g.add_edge(edge[0],edge[1])
g.print_graph()