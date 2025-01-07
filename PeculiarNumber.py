def find_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def peculiar_number(N, K, arr):
    # Step 1: Replace elements with the absolute difference between element and index
    replaced_arr = [abs(arr[i] - i) for i in range(N)]
    
    # Step 2: Partition the array into K parts minimizing the maximum sum
    def can_partition(max_sum):
        partition_count = 1
        current_sum = 0
        for num in replaced_arr:
            if current_sum + num > max_sum:
                partition_count += 1
                current_sum = num
                if partition_count > K:
                    return False
            else:
                current_sum += num
        return True
    
    # Binary search for the smallest possible maximum sum
    left, right = max(replaced_arr), sum(replaced_arr)
    while left < right:
        mid = (left + right) // 2
        if can_partition(mid):
            right = mid
        else:
            left = mid + 1
    
    max_partition_sum = left
    
    # Step 3: Find Fibonacci number or return the sum
    if max_partition_sum < 100:
        return find_fibonacci(max_partition_sum)
    else:
        return max_partition_sum

# Taking single input for N, K, and arr
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# Output the peculiar number
print(peculiar_number(N, K, arr))
