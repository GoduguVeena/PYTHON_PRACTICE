def good_sum(N, A):
    stack = []
    for x in A:
        if x < 0:
            abs_x = abs(x)
            sum_removed = 0
            
            # Remove elements from the stack until the sum of removed elements is >= abs(x)
            while stack and sum_removed < abs_x:
                sum_removed += stack.pop()
                
            # Convert x to its absolute value
            stack.append(abs_x)
        else:
            stack.append(x)
    
    return sum(stack)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the integer N
    A = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and print the output
    result = good_sum(N, A)
    print(result)

if __name__ == "__main__":
    main()
