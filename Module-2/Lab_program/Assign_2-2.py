fruits = ["Apple", "Banana", "Cherry"]
print("Original list:", fruits)

fruits.append("Mango")
print("\nAfter append('Mango'):", fruits)

fruits.insert(1, "Orange")  
print("After insert(1, 'Orange'):", fruits)

fruits.remove("Banana")
print("After remove('Banana'):", fruits)

popped_item = fruits.pop()  
print("After pop():", fruits)
print("Popped element:", popped_item)
