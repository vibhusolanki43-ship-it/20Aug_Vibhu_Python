student_info = {
    "name": "Vibhu",
    "age": 15,
    "grade": "12th",
    "school": "Skp School",
    "city": "Rajkot",
    "sports": "cricket"
}

print("Original dictionary:")
print(student_info)

student_info["age"] = 17  
student_info["city"] = "Surat"  

print("\nDictionary after updating values:")
print(student_info)

student_info.update({"grade": "8th", "sports": "Cricket"})

print("\nDictionary after using update() method:")
print(student_info)
