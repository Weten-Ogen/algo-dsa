class Vertex:
    def __init__(self, n):
        self.name = n

class Graph:
    vertices = {}
    edges = []
    edges_indices = {}


    def add_vertex(self , vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edges_indices[vertex.name] =len(self.edges_indices)
            return True
        else:
            return False

    def add_edge(self, u, v,weight=1):
        if u in  self.vertices and v in self.vertices:
            self.edges[self.edges_indices[u]][self.edges_indices[v]] = weight
            self.edges[self.edges_indices[v]][self.edges_indices[u]] = weight
            return True
        else:
            return False
    
    def print_graph(self):
        for v , i in sorted(self.edges_indices.items()):
            print(v +  ' ' , end = ' ')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end=' ')
            print()


graph = Graph()

graph.print_graph()