def highest_altitude(n, l):
    current_altitude = 0
    max_altitude = 0

    for gain in l:
        current_altitude += gain
        if current_altitude > max_altitude:
            max_altitude = current_altitude

    return max_altitude

if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    result = highest_altitude(n, l)
    print(result)