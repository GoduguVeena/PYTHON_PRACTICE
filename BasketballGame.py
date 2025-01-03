def calculate_score(ops):
    stack = []
    for op in ops:
        if op == 'C':
            if stack:
                stack.pop()
        elif op == 'D':
            if stack:
                stack.append(2 * stack[-1])
        elif op == '+':
            if len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    return sum(stack)

# Input
n = int(input().strip())
ops = input().strip().split()

# Calculate and output the score
print(calculate_score(ops))
