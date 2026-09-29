import sys


def solve():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line.strip())

    numbers = []
    while len(numbers) < n:
        parts = sys.stdin.readline().split()
        for x in parts:
            numbers.append(int(x) - 1)

    f = numbers

    for a in range(n):
        b = f[a]
        c = f[b]
        if f[c] == a:
            print("YES")
            return

    print("NO")


if __name__ == "__main__":
    solve()