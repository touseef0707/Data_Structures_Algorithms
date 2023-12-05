
class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = edges
        self.data = [[] for i in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def bfs(self, root):
        queue = []
        discovered = [False] * len(self.data)
        distance = [None] * len(self.data)
        parent = [None] * len(self.data)

        discovered[root] = True
        distance[root] = 0
        queue.append(root)
        idx = 0

        while idx < len(queue):
            current = queue[idx]
            idx += 1

            for node in self.data[current]:
                if not discovered[node]:
                    discovered[node] = True
                    distance[node] = 1 + distance[current]
                    parent[node] = current
                    queue.append(node)

        return set(queue), distance, parent

    def is_all_connected(self):
        if len(self.bfs(0)[0]) < len(self):
            return False
        return True

    def components(self):
        components = []
        a = []
        for i in range(len(self.data)):
            if i not in a:
                a = self.bfs(i)[0]
                # print(a)
                components.append(a)
        return components

    def dfs(self, root):
        stack = []
        discovered = [False] * len(self.data)
        stack.append(root)
        result = []
        while len(stack) > 0:
            current = stack.pop()
            if not discovered[current]:
                discovered[current] = True
                result.append(current)
                for node in self.data[current]:
                    if not discovered[node]:
                        stack.append(node)
        return result

    def dfs_cycle(self, node, discovered, parent):
        discovered[node] == True
        for i in self.data[node]:
            if discovered[i] == False:
                if (self.dfs_cycle(i, discovered, node)) == True:
                    return True
            elif parent != i:
                return True
        return False

    def is_cyclic(self):
        discovered = [False] * len(self.data)
        for i in range(len(self.data)):
            if discovered[i]==False:
                if self.dfs_cycle(i, discovered, -1) == True:
                    return True
        return False

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return "\n".join(["{}: {}".format(node, neighbours) for node, neighbours in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

num_nodes1 = 5
edges1 = [(0, 1), (0, 4), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4)]
graph1 = Graph(num_nodes1, edges1)
# print(graph1)

# Question: Write a program to check if all the nodes in a graph are connected

num_nodes2 = 9
edges2 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]
graph2 = Graph(num_nodes2, edges2)
print(graph2)
graph2.is_cyclic()
"""
print(graph2)
print("Is the graph connected:",graph2.is_all_connected())
print("Number of Nodes:",len(graph2))
components = graph2.components()
print(components,"\nNumber of connected components: ",len(components))
print(graph1.dfs(0))
print("Is Graph 1 cyclic: ",graph1.is_cyclic())
"""



