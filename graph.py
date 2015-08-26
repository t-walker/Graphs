class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """Creates a new graph.
           vs is a list of verticies
           es is a list of edges."""
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)
        return

    def add_vertex(self, v):
        """Add 'v' to the graph."""
        self[v] = {}


    def add_edge(self, e):
        """Add 'e' to the graph by adding an entry in both directions."""
        v, w = e
        self[v][w] = e


    def get_edge(self, t):
        v1 = t[0] # Vertex 1
        v2 = t[1] # Vertex 2

        try:
            e = self[v1][v2]
        except:
            e = self[v2][v1]
        finally:
            print("Edge does not exist for %s and %s." %s (v1, v2))

        return e

    def verticies(self):
        return list(self.keys())

    def edges(self):
        return list(self.values())

    def remove_edge(self, e):
        v1 = e[0]
        v2 = e[1]

        self[v1][v2] = None
        self[v2][v1] = None
