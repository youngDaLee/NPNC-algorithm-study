def dfs(visited, computers, v):
    visited[v] = True
    for i,  conn in enumerate(computers[v]):
        if conn == 1:
            if not visited[i]:
                visited = dfs(visited, computers, i)

    return visited

def solution(n, computers):
    answer = 0
    visited = [False]*n

    for i in range(n):
        if not visited[i]:  # 방문 안했으면
            visited = dfs(visited, computers, i)  # dfs로 연결된 컴퓨터 방문처리
            answer += 1

    return answer
