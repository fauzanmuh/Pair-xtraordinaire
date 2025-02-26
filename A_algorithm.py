import heapq

def heuristic(a, b):
    """Menghitung jarak Manhattan sebagai heuristic"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    """Implementasi algoritma A* untuk pencarian jalur"""
    rows, cols = len(grid), len(grid[0])
    open_set = []  # Priority queue untuk node yang akan dievaluasi
    heapq.heappush(open_set, (0, start))

    came_from = {}  # Melacak jalur
    g_score = {node: float('inf') for row in grid for node in enumerate(row)}
    g_score[start] = 0

    f_score = {node: float('inf') for row in grid for node in enumerate(row)}
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        neighbors = get_neighbors(current, rows, cols)
        for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] == 1:  # Tidak bisa melewati rintangan
                continue

            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # Jika tidak ada jalur yang ditemukan

def reconstruct_path(came_from, current):
    """Membangun ulang jalur dari titik awal ke tujuan"""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def get_neighbors(node, rows, cols):
    """Mengembalikan tetangga yang valid"""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for d in directions:
        neighbor = (node[0] + d[0], node[1] + d[1])
        if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
            neighbors.append(neighbor)
    return neighbors

# Contoh penggunaan grid:
# 0 = jalan, 1 = rintangan
example_grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start_point = (0, 0)  # Titik awal
goal_point = (4, 4)   # Titik tujuan

path = a_star_search(example_grid, start_point, goal_point)
if path:
    print("Jalur terpendek:", path)
else:
    print("Tidak ada jalur yang tersedia")
