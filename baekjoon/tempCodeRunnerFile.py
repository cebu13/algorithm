# 11724
import sys

N, M = map(int, sys.stdin.readline().split())
A = [[]*(N+1)]
count = 0

visited = [False] * (N+1)


def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)


for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    A[s].append(e)
    A[e].append(s)

for i in range(1, N+1):
    if not visited[i]:
        count += 1
        DFS[i]
print(count)
