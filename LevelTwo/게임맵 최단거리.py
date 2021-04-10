from collections import deque

def bfs(start, maps):
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    queue = deque()
    queue.append(start)
    print(queue)
    while queue:
        y, x, cnt = queue.popleft()
        maps[y][x] = 0
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            
            # 현재 위치에서 다음 위치로 이동했을 때 목적지면, 
            # 지금까지의 count + 1을 반환한다.
            if ny == len(maps)-1 and nx == len(maps[0])-1:
                return cnt + 1
            
            # visited 사용할 필요 없이, 한번 온 길을 다시 돌아갈 수 없게
            # maps의 해당 좌표값을 0으로 만들면 된다.
            elif 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                queue.append((ny, nx, cnt+1))
            
    return -1    
    
def solution(maps):
    # 현재 위치도 칸 1개를 차지하므로, count를 1부터 시작한다.
    return bfs((0,0,1), maps)
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))