from collections import deque


def find_path(graph, u, v, avoid_vertices):  # обход в ширину
    visited = set()
    queue = deque([(u, [(u, 0)])])

    while queue:
        print(f'visited = {visited}')
        print(f'queue = {queue}')
        current, path = queue.popleft()
        print('Текущий и путь')
        print(current)
        print(path)
        visited.add(current)

        if current == v:
            return path

        for neighbor, weight in graph.get(current, {}).items():
            print(neighbor, weight)
            print(visited, avoid_vertices)
            if neighbor not in visited and neighbor not in avoid_vertices:
                new_path = path + [(neighbor, weight)]
                queue.append((neighbor, new_path))

    return None


# def find_path(graph, u, v, avoid_vertices):  # обход в глубину
#     visited = set()
#
#     def dfs(current, path):
#         visited.add(current)
#         print(f'path = {path}')
#         print(f"Current = {current}")
#         if current == v:
#             return path
#         print(graph.get(current, {}))
#         for neighbor, weight in graph.get(current, {}).items():
#             print(neighbor, weight)
#             print(visited, avoid_vertices)
#             if neighbor not in visited and neighbor not in avoid_vertices:
#                 print('заход в дфс')
#                 result = dfs(neighbor, path + [(neighbor, weight)])
#                 if result:
#                     return result
#         return None
#
#     return dfs(u, [(u, '0')]) if u in graph and v in graph else None


a = {'1': {'1': '10', '3': '4', '2': '3', '7': '4'},
     '3': {'5': '4'},
     '2': {'3': '11', '5': '6', '4': '2'},
     '7': {'4': '5', '8': '9', '6': '3'},
     '5': {'7': '3'},
     '4': {'3': '2', '7': '4'},
     '6': {'8': '1'},
     '8': {'1': '100'}
     }


print(find_path(a, '1', '8', ['3', '5']))
