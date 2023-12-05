class Graphs:

    def __init__(self, num_nodes, edges, directed=False):
        self.num_nodes = num_nodes
        self.edges = edges
        self.directed = directed
        self.weighted = len(edges) > 0 and (len(edges[0])==3)
        self.data = [[] for i in range(num_nodes)]
        self.weight = [[] for i in range(num_nodes)]

        for e in edges:
            self.data[e[0]].append(e[1])
            if self.weighted:
                self.weight[e[0]].append(e[2])
            if not directed:
                self.data[e[1]].append(e[0])
                if self.weighted:
                    self.weight[e[1]].append(e[2])

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (node, weight) in enumerate(zip(self.data, self.weight)):
                result += "{}: {}\n".format(i, list(zip(node, weight)))
        else:
            for i, node in enumerate(self.data):
                result += "{}: {}\n".format(i, node)

        return result

num_nodes1 = 9
edges1 = [(0, 1, 3), (0, 3, 2), (1, 7, 4), (7, 2, 2), (3, 2, 6),
          (2, 5, 1), (5, 6, 8), (3, 4, 1), (4, 8, 0), (8, 0, 4)]
graph1 = Graphs(num_nodes1, edges1, directed=False)
# print(graph1)

num_nodes2 = 5
edges2 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
graph2 = Graphs(num_nodes2, edges2, directed = True)
print(graph2)