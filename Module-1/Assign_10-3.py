numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(num):
    return num % 2 == 0

even_numbers = filter(is_even, numbers)
even_numbers_list = list(even_numbers)
print("Original numbers:", numbers)
print("Even numbers:", even_numbers_list)
