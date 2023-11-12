a = {
    '1': {'2': None, '3': None},
    '2': {'2': None, '5': None},
    '3': {'4': None},
    '4': {'3': None, '2': None},
    '5': {'1': None}
}

in_degree = {vertex: 0 for vertex in a}
out_degree = {vertex: 0 for vertex in a}

for vertex in a:
    for neighbor in a[vertex]:
        print(neighbor)
        # Исходящая степень
        out_degree[vertex] += 1
        # Входящая степень, исключая петли
        if neighbor != vertex:
            in_degree[neighbor] += 1

# Вывод степени каждой вершины
for vertex in a:
    print(f"Вершина {vertex}: Входящая степень = {in_degree[vertex]}, Исходящая степень = {out_degree[vertex]}")
    print(f'Общая степень вершины: {in_degree[vertex] + out_degree[vertex]}')



# # Создаем словарь для хранения степеней каждой вершины
# degrees = {}
#
# # Перебираем каждую вершину
# for vertex in a:
#     # Инициализируем степень для текущей вершины
#     degree = 0
#
#     # Считаем исходящие рёбра
#     if vertex in a:
#         degree += len(a[vertex])
#
#     # Считаем входящие рёбра
#     for v in a:
#         print(a[v])
#         if vertex in a[v]:
#             degree += 1
#
#     # Сохраняем степень для текущей вершины
#     degrees[vertex] = degree
#
# # Выводим степени каждой вершины
# for vertex, degree in degrees.items():
#     print(f'Вершина {vertex} имеет степень {degree}')
