def replace_greater_than_ten(numbers):
    # Replace elements greater than 10 with '*'
    new_numbers = ['*' if n > 10 else n for n in numbers]
    print(new_numbers)

# Test cases
numbers1 = [30, 1, 20, 4]
replace_greater_than_ten(numbers1)  # Output: ['*', 1, '*', 4]

numbers2 = [5, 9, 11, 23]
replace_greater_than_ten(numbers2)  # Output: [5, 9, '*', '*']
