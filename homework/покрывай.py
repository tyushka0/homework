import sys
from collections import deque


def solve():
    input = sys.stdin.readline

    first_line = input()
    if not first_line:
        return
    t = int(first_line.strip())

    for _ in range(t):
        line = input().split()
        while not line:
            line = input().split()
        n, m = map(int, line)

        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        dist = [-1] * (n + 1)
        queue = deque([1])
        dist[1] = 0

        even_set = []
        odd_set = []

        while queue:
            v = queue.popleft()
            if dist[v] % 2 == 0:
                even_set.append(v)
            else:
                odd_set.append(v)

            for to in adj[v]:
                if dist[to] == -1:
                    dist[to] = dist[v] + 1
                    queue.append(to)

        ans = even_set if len(even_set) <= len(odd_set) else odd_set

        print(len(ans))
        print(*(ans))


if __name__ == '__main__':
    solve()