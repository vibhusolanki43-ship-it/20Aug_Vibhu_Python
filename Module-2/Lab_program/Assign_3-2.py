numbers = [25, 10, 45, 30, 5, 60]

print("Original list:", numbers)

numbers.sort()
print("\nList after using sort():", numbers)

numbers2 = [25, 10, 45, 30, 5, 60]
sorted_list = sorted(numbers2)
print("\nOriginal list (unchanged):", numbers2)
print("New sorted list (using sorted()):", sorted_list)

descending_list = sorted(numbers2, reverse=True)
print("\nList sorted in descending order:", descending_list)

