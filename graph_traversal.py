import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict, deque

class GraphVisualizer:
    def __init__(self):
        self.graph = defaultdict(list)
        self.G = nx.Graph()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.G.add_edge(u, v)

    def dfs(self, start, visited=None, pos=None):
        if visited is None:
            visited = set()
        if pos is None:
            pos = nx.spring_layout(self.G)

        visited.add(start)
        print(start, end=" ")
        self._visualize(pos, visited)

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, pos)
        return visited

    def bfs(self, start):
        visited = set([start])
        queue = deque([start])
        pos = nx.spring_layout(self.G)

        while queue:
            node = queue.popleft()
            print(node, end=" ")
            self._visualize(pos, visited)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def is_connected(self):
        visited = self.dfs(list(self.graph.keys())[0])
        return len(visited) == len(self.graph)

    def _visualize(self, pos, visited):
        plt.clf()  # Clear previous plots
        nx.draw(self.G, pos, with_labels=True, node_color=['green' if node in visited else 'red' for node in self.G.nodes()])
        plt.draw()
        plt.pause(0.5)

# Example usage with visualizer
if __name__ == "__main__":
    gv = GraphVisualizer()
    gv.add_edge(0, 1)
    gv.add_edge(0, 2)
    gv.add_edge(1, 3)
    gv.add_edge(2, 3)
    gv.add_edge(3, 4)

    plt.ion()  # Interactive mode ON
    print("DFS Traversal with Visualization:")
    gv.dfs(0)

    print("\nBFS Traversal with Visualization:")
    gv.bfs(0)

    plt.ioff()  # Turn off interactive mode
    plt.show()  # Display the final plot
