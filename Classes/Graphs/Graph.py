from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.weights = defaultdict(int)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source, destination, weight):
        if source in self.graph and destination in self.graph:
            self.graph[source].append((destination, weight))

    def remove_edge(self, source, destination):
        if source in self.graph:
            self.graph[source] = [(neighbor, weight) for neighbor, weight in self.graph[source] if not neighbor == destination]

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])

    def get_vertices(self):
        return list(self.graph.keys())

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]

            for key in self.graph:
                self.graph[key] = [(neighbor, weight) for neighbor, weight in self.graph[key] if not neighbor == vertex]

    def dfs(self, start, goal):
        if start not in self.graph:
            print(f"The starting vertex {start} is not present in the graph.")
            return [], []

        stack = deque()
        parents = {}
        self.weights.clear()

        stack.append(start)
        parents[start] = None

        steps = []

        while stack:
            current_vertex = stack.pop()
            current_step = [current_vertex]

            for neighbor, weight in self.graph[current_vertex]:
                if neighbor not in parents:
                    stack.append(neighbor)
                    parents[neighbor] = current_vertex
                    self.weights[neighbor] = weight

                    # Add the vertex to the current step
                    current_step.append(neighbor)
                else:
                    if weight < self.weights[neighbor]:
                        self.weights[neighbor] = weight
                        parents[neighbor] = current_vertex

            # Add the current step to the list of steps
            steps.append(list(current_step))

        best_path = self.build_path(parents, goal)
        return best_path, steps

    def print_dfs_steps(self, steps):
        print("Depth-First Search (DFS) Steps:")
        for i, step in enumerate(steps):
            print(f"Step {i + 1}: { ' -> '.join(map(str, step)) }")

    def build_path(self, parents, goal):
        path = []

        current = goal
        while current is not None:
            path.insert(0, current)

            # Check if the key is present in the dictionary
            if current in parents:
                current = parents[current]
            else:
                # Handle the case where the key is not present
                break

        return path

    def get_adjacency_matrix(self):
        matrix_strings = []
        num_vertices = len(self.graph)

        header = f"   {' '.join(map(str, self.graph.keys()))}"
        matrix_strings.append(header)

        for vertex in self.graph.keys():
            row = f"{vertex} "
            for other_vertex in self.graph.keys():
                has_edge = any(edge[0] == other_vertex for edge in self.graph[vertex])
                row += "1 " if has_edge else "0 "
            matrix_strings.append(row.rstrip())

        return matrix_strings

    def get_all_vertices(self):
        vertices = list(self.graph.keys())
        print("All vertices in the graph: " + ", ".join(map(str, vertices)))
        return vertices
