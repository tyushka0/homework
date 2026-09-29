import sys

sys.setrecursionlimit(3000)


def main():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
    except (ValueError, IndexError):
        return


    p = []
    while len(p) < n:
        parts = sys.stdin.readline().split()
        for x in parts:
            p.append(int(x))

    memo = {}

    def get_depth(u):
        if u in memo:
            return memo[u]

        manager = p[u - 1]
        if manager == -1:
            memo[u] = 1
        else:
            memo[u] = 1 + get_depth(manager)

        return memo[u]

    max_groups = 0
    for i in range(1, n + 1):
        depth = get_depth(i)
        if depth > max_groups:
            max_groups = depth

    print(max_groups)


if __name__ == "__main__":
    main()