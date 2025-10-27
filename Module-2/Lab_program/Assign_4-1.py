mixed_tuple = (25, "Hello", 3.14, True, None, [1, 2, 3], {'a': 10, 'b': 20})

print("Tuple with multiple data types:")
print(mixed_tuple)

print("\nData types of each element in the tuple:")
for item in mixed_tuple:
    print(f"{item}-{type(item)}")
