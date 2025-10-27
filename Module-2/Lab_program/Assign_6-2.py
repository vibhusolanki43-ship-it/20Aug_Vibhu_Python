# Program to access dictionary values using keys

# Creating a sample dictionary
student_info = {
    "name": "Vibhu",
    "age": 17,
    "grade": "12th",
    "school": "Skp School",
    "city": "Rajkot",
    "sports": "Cricket"
}

print("Accessing dictionary values using keys:")
print("Name:", student_info["name"])
print("Age:", student_info["age"])
print("Grade:", student_info["grade"])
print("School:", student_info["school"])
print("City:", student_info["city"])
print("Sports:", student_info["sports"])

print("\nAccessing using get() method:")
print("Name:", student_info.get("name"))
print("Country (not in dictionary):", student_info.get("country", "Not Found"))
