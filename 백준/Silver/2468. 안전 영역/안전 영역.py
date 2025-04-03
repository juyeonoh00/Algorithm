from collections import deque

# 입력 받기
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

# 이동 방향 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# BFS 함수
def bfs(x, y, visited, rain_height):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx] and area[ny][nx] > rain_height:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

# 지역에서 가장 높은 높이 찾기
max_height = max(max(row) for row in area)

max_safe_area = 0

# 비의 양을 0부터 최대 높이까지 변화시키면서 안전 영역 개수 구하기
for rain in range(0, max_height + 1):
    visited = [[False] * N for _ in range(N)]
    safe_area_count = 0

    for y in range(N):
        for x in range(N):
            if not visited[y][x] and area[y][x] > rain:
                bfs(x, y, visited, rain)
                safe_area_count += 1

    max_safe_area = max(max_safe_area, safe_area_count)

# 결과 출력
print(max_safe_area)
