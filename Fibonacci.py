def extract_numbers(s):
    import re
    return list(map(int, re.findall(r'\d+', s)))

def is_fibonacci(n):
    if n == 0 or n == 1:
        return True
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def fibonacci_sequence(k):
    seq = [0, 1]
    while len(seq) < k:
        seq.append(seq[-1] + seq[-2])
    return seq[:k]

def optimal_fibonacci_count(s):
    numbers = extract_numbers(s)
    fibonacci_numbers = [num for num in numbers if is_fibonacci(num)]
    count = len(fibonacci_numbers)
    
    if count == 0:
        return "0"
    else:
        result = [str(count)]
        result.append(" ".join(map(str, fibonacci_numbers)))
        result.append(" ".join(map(str, fibonacci_sequence(count))))
        return "\n".join(result)

if __name__ == '__main__':
    s = input().strip()
    print(optimal_fibonacci_count(s))
