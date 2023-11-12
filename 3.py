class Graph:
    def __init__(self, directed, weight):
        self.adjacency_list = {}
        self.directed = directed  # Флаг для указания на ориентированный граф
        self.weight = weight      # Флаг для указания на взвешенный граф

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}
        else:
          print("Введенная вершина уже существует.")

    def add_vertex_from_file(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight=None):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1][vertex2] = weight
            if not self.directed:
                self.adjacency_list[vertex2][vertex1] = weight
        else:
            print("Ошибка: Одна или обе вершины не существуют в графе.")

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            for v in self.adjacency_list:
                if vertex in self.adjacency_list[v]:
                    del self.adjacency_list[v][vertex]
        else:
            print("Ошибка: Вершина не существует в графе.")

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                del self.adjacency_list[vertex1][vertex2]
            if not self.directed and vertex1 in self.adjacency_list[vertex2]:
                del self.adjacency_list[vertex2][vertex1]
        else:
            print("Ошибка: Одна или обе вершины не существуют в графе.")

    def print_adjacency_list(self):
        for vertex, neighbors in self.adjacency_list.items():
            print(f"Вершина {vertex}: {neighbors}")
