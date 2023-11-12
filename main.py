import copy
from collections import deque


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

    def print_degree_vertexes(self):
        in_degree = {vertex: 0 for vertex in self.adjacency_list}
        out_degree = {vertex: 0 for vertex in self.adjacency_list}

        for vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                # Исходящая степень
                out_degree[vertex] += 1
                # Входящая степень, исключая петли
                if neighbor != vertex:
                    in_degree[neighbor] += 1

        # Вывод степени каждой вершины
        for vertex in self.adjacency_list:
            print(f"Вершина {vertex}: Входящая степень = {in_degree[vertex]}, Исходящая степень = {out_degree[vertex]}")
            print(f'Общая степень вершины: {in_degree[vertex] + out_degree[vertex]}')

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    vertices = line.strip().split()
                    if self.weight is False:
                        vertex1, vertex2 = vertices[0], vertices[1]
                        weight = None
                    else:
                        vertex1, vertex2 = vertices[0], vertices[1]
                        weight = vertices[2]
                    self.add_vertex_from_file(vertex1)
                    self.add_vertex_from_file(vertex2)
                    self.add_edge(vertex1, vertex2, weight)
        except FileNotFoundError:
            print(f"Ошибка: Файл '{filename}' не найден.")

    def save_to_file(self, filename):
        try:
            with open(filename, "w") as file:
                for vertex, neighbors in self.adjacency_list.items():
                    for neighbor, weight in neighbors.items():
                        if weight is not None:
                            file.write(f"{vertex} {neighbor} {weight}\n")
                        else:
                            file.write(f"{vertex} {neighbor}\n")
        except IOError:
            print(f"Ошибка: Не удалось сохранить в файл '{filename}'.")

    def neighbors_vertex(self, v):
        neighbors_list = []
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                if neighbor == v:
                    neighbors_list.append(vertex)
        print(f'В вершину {v} заходят вершины {", ".join(neighbors_list)} ')

    def complete_to_full_graph(self):
        my_dict = {}
        vertexes_list = [v for v in self.adjacency_list]
        for vertex in vertexes_list:
            neighbors = {v: None for v in self.adjacency_list if v != vertex}
            my_dict[vertex] = neighbors
        self.adjacency_list = my_dict
        for vertex, neighbors in self.adjacency_list.items():
            print(f"Вершина {vertex}: {neighbors}")

    def find_path_bfs(self, u, v, avoid_vertexes):  # обход в ширину
        visited = set()
        queue = deque([(u, [(u, '0')])])

        while queue:
            current, path = queue.popleft()
            visited.add(current)

            if current == v:
                return path

            for neighbor, weight in self.adjacency_list.get(current, {}).items():
                if neighbor not in visited and neighbor not in avoid_vertexes:
                    new_path = path + [(neighbor, weight)]
                    queue.append((neighbor, new_path))

        return None

    def find_path_dfs(self, u, v, avoid_vertexes):  # обход в глубину
        visited = set()

        def dfs(current, path):
            visited.add(current)
            if current == v:
                return path
            for neighbor, weight in self.adjacency_list.get(current, {}).items():
                if neighbor not in visited and neighbor not in avoid_vertexes:
                    result = dfs(neighbor, path + [(neighbor, weight)])
                    if result:
                        return result
            return None

        return dfs(u, [(u, '0')]) if u in self.adjacency_list and v in self.adjacency_list else None


if __name__ == "__main__":
    my_graph = None  # Изначально граф не создан
    copied_graph = None  # Изначально копия графа не создана

    while True:
        print("\nМеню:")
        print("1. Создать новый граф")
        print("2. Добавить вершину")
        print("3. Добавить ребро")
        print("4. Удалить вершину")
        print("5. Удалить ребро")
        print("6. Вывести список смежности")
        print("7. Загрузить граф из файла")
        print("8. Сохранить граф в файл")
        print("9. Создать копию графа")
        print("10. Вывести копию графа")
        print("11. Удалить граф и его копию")
        print("12. Вывести степень каждой вершины (задание 2.5)")
        print("13. Вывести все заходящие соседние вершины в выбранную вершину (задание 3.11) ")
        print("14. Построить полный граф на основе данного графа (задание 4.1)")
        print("""15. Найти путь, соединяющий вершины u и v и не проходящий через заданное подмножество вершин V (задание 5.9, обход в глубину) (загрузи 3.txt)""")
        print("""16. Найти путь, соединяющий вершины u и v и не проходящий через заданное подмножество вершин V (задание 5.9, обход в ширину) (загрузи 3.txt)""")
        print("17. Выход")

        choice = input("Введите номер операции: ")

        if choice == "1":
            directed = True if input("Создать ориентированный граф (da/net)? ").strip().lower() == 'da' else False
            weight = True if input("Создать взвещенный граф (da/net)? ").strip().lower() == 'da' else False
            my_graph = Graph(directed, weight)
            copied_graph = None  # При создании нового графа удаляем существующую копию
        elif my_graph is None:
            print("Ошибка: Сначала создайте граф (пункт 1)")
        elif choice == "2":
            vertex = input("Введите номер вершины: ")
            my_graph.add_vertex(vertex)
        elif choice == "3":
            vertex1 = input("Введите номер первой вершины: ")
            vertex2 = input("Введите номер второй вершины: ")
            if my_graph.weight == 'da':
                weight = input("Введите вес ребра: ") or '0'
            else:
                weight = None
            my_graph.add_edge(vertex1, vertex2, weight)
        elif choice == "4":
            try:
                vertex = input("Введите номер вершины для удаления: ")
                my_graph.remove_vertex(vertex)
            except ValueError:
                print("Ошибка: Неверный формат вершины. Введите целое число.")
        elif choice == "5":
            vertex1 = input("Введите номер первой вершины: ")
            vertex2 = input("Введите номер второй вершины: ")
            my_graph.remove_edge(vertex1, vertex2)
        elif choice == "6":
            my_graph.print_adjacency_list()
        elif choice == "7":
            filename = input("Введите имя файла для загрузки: ")
            my_graph.load_from_file(filename)
        elif choice == "8":
            filename = input("Введите имя файла для сохранения: ")
            my_graph.save_to_file(filename)
        elif choice == "9":
            if my_graph is not None:
                copied_graph = copy.deepcopy(my_graph)  # Создаем копию графа
                print("Создана копия графа.")
        elif choice == "10":
            if copied_graph is not None:
                print("Копия графа:")
                copied_graph.print_adjacency_list()
        elif choice == "11":
            my_graph = None  # Удаляем текущий граф
            copied_graph = None  # Удаляем текущую копию графа
            print("Граф и его копия удалены.")
        elif choice == "12":
            my_graph.print_degree_vertexes()
        elif choice == "13":
            vertex = input("Введите вершину: ")
            my_graph.neighbors_vertex(vertex)
        elif choice == '14':
            copied_graph = copy.deepcopy(my_graph)
            copied_graph.complete_to_full_graph()
        elif choice == '15':
            vertex1 = input("Введите первую вершину: ")
            vertex2 = input("Введите вторую вершину: ")
            avoid_vertexes = input("Введите подмножество вершин, которые надо избегать (в строчку через пробел): ")
            avoid_vertexes = avoid_vertexes.split()
            print(my_graph.find_path_dfs(vertex1, vertex2, avoid_vertexes))
        elif choice == '16':
            vertex1 = input("Введите первую вершину: ")
            vertex2 = input("Введите вторую вершину: ")
            avoid_vertexes = input("Введите подмножество вершин, которые надо избегать (в строчку через пробел): ")
            avoid_vertexes = avoid_vertexes.split()
            print(my_graph.find_path_bfs(vertex1, vertex2, avoid_vertexes))
        elif choice == "17":
            print("Всем пока :)")
            break
