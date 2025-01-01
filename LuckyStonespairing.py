def countLuckyPairs(p, n, m, v):
    count = 0
    
    # Iterate through all unique pairs of stones
    for i in range(p):
        for j in range(i + 1, p):
            if (v[i] % n == 0 or v[i] % m == 0) and (v[j] % n == 0 or v[j] % m == 0):
                count += 1
    
    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    p = int(data[0])
    n = int(data[1])
    m = int(data[2])
    v = list(map(int, data[3:]))
    ans = countLuckyPairs(p, n, m, v)
    print(ans)
