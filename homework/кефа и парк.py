import sys


def solve():
    input = sys.stdin.readline

    first_line = input().split()
    if not first_line:
        return
    n, m = map(int, first_line)

    cats = [0] + list(map(int, input().split()))

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    ans = 0

    init_cats = 1 if cats[1] == 1 else 0
    if init_cats > m:
        print(0)
        return

    stack = [(1, 0, init_cats)]

    while stack:
        u, p, cur_cats = stack.pop()

        is_leaf = True
        for to in adj[u]:
            if to != p:
                is_leaf = False
                nxt_cats = cur_cats + 1 if cats[to] == 1 else 0

                if nxt_cats <= m:
                    stack.append((to, u, nxt_cats))

        if is_leaf and u != 1:
            ans += 1

    print(ans)


if __name__ == "__main__":
    solve()