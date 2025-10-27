keys = ["name", "age", "grade", "city"]
values = ["Vibhu", 17, "12th", "Ahmedabad"]

merged_dict = {}

for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

print("Merged dictionary:")
print(merged_dict)
