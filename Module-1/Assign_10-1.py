numbers = [1, 2, 3, 4, 5]

def square(num):
    return num ** 2

squared_numbers = map(square, numbers)

squared_numbers_list = list(squared_numbers)
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers_list)
