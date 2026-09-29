import sys
import heapq

def main():
    def token_generator():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = token_generator()

    try:
        n_str = next(tokens)
    except StopIteration:
        return

    n = int(n_str)
    m = int(next(tokens))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(tokens))
        v = int(next(tokens))
        w = int(next(tokens))
        if u != v:
            adj[u].append((v, w))
            adj[v].append((u, w))

    INF = 10**18
    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)

    dist[1] = 0
    pq = [(0, 1)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue
        if u == n:
            break

        for v, w in adj[u]:
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))

    if dist[n] == INF:
        print(-1)
        return

    path = []
    curr = n
    while curr != -1:
        path.append(curr)
        curr = parent[curr]

    path.reverse()
    print(*(path))

if __name__ == '__main__':
    main()