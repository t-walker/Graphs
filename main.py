from edge import Edge
from graph import Graph
from vertex import Vertex

def main():
    v = Vertex('v')
    w = Vertex('w')
    a = Vertex('a')
    e = Edge(v,w)
    e2 = Edge(w,v)

    g = Graph([v,w], [e])
    g.add_edge(e2)
    print(g.verticies())
    print(g.edges())

if __name__ == "__main__":
    main()
