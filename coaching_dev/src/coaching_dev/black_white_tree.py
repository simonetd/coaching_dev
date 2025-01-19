"""https://www.hackerrank.com/challenges/black-n-white-tree-1/problem"""

from collections import defaultdict, deque
import itertools

class BlackAndWhiteTreeSolver:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def bfs_component(self, start, visited):
        """Perform BFS to find a connected component."""
        queue = deque([start])
        component = []
        visited[start] = True
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return component

    def find_components(self):
        """Find all connected components in the graph."""
        visited = [False] * (self.n + 1)
        components = []

        for node in range(1, self.n + 1):
            if not visited[node]:
                component = self.bfs_component(node, visited)
                components.append(component)

        return components

    def bipartite_check(self, component):
        """Check if a component is bipartite and return the node groups."""
        colors = {}
        queue = deque([component[0]])
        colors[component[0]] = 0
        group1, group2 = [], []

        while queue:
            node = queue.popleft()
            (group1 if colors[node] == 0 else group2).append(node)
            for neighbor in self.graph[node]:
                if neighbor not in colors:
                    colors[neighbor] = 1 - colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return None  # Not bipartite

        return group1, group2

    def minimal_difference_coloring(self):
        """Solve the problem and return the results."""
        components = self.find_components()

        added_edges = []
        total_group1, total_group2 = [], []

        for component in components:
            result = self.bipartite_check(component)
            if not result:
                raise ValueError("Graph is not bipartite, input constraints violated.")
            group1, group2 = result
            total_group1.extend(group1)
            total_group2.extend(group2)

        # Connect components
        for i in range(len(components) - 1):
            u = components[i][0]
            v = components[i + 1][0]
            added_edges.append((u, v))
            self.graph[u].append(v)
            self.graph[v].append(u)

        diff = abs(len(total_group1) - len(total_group2))
        return diff, len(added_edges), added_edges

    @staticmethod
    def tree_generator(n):
        """Generate a tree structure for testing."""
        return [(i, i // 2) for i in range(2, n + 1)]

if __name__ == "__main__":
    # Example Usage
    n = 8
    edges = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 5), (2, 6), (3, 7), (4, 8)]

    solver = BlackAndWhiteTreeSolver(n, edges)
    diff, added_count, added_edges = solver.minimal_difference_coloring()
    print(diff, added_count)
    for u, v in added_edges:
        print(u, v)

    # Generate a tree for testing
    generated_tree = BlackAndWhiteTreeSolver.tree_generator(32)
    print("Generated Tree:", generated_tree)
