# Enter your code here. Read input from STDIN. Print output to STDOUT
def push_zeroes_to_end(arr):
    n = len(arr)
    result = []
    
    # Collect all non-zero elements
    for num in arr:
        if num != 0:
            result.append(num)
    
    # Count the number of zeroes
    zero_count = n - len(result)
    
    # Append the zeroes at the end
    result.extend([0] * zero_count)
    
    return result

# Input
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Output
result = push_zeroes_to_end(arr)
print(*result)
