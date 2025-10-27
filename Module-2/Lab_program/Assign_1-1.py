mixed_list = [
    42,              
    "Hello Python",  
    3.14159,         
    True,            
    (1, 2, 3),       
    {'a': 10, 'b': 20}, 
    [5, 6]           
]

print("The created list is:")
print(mixed_list)

print("-" * 30)
print("Elements and their data types:")
for element in mixed_list:
    print(f"{element}, Type: {type(element).__name__}")