percentage = float(input("Enter your percentage: "))

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F (Fail)"

print("Your Percentage:", percentage)
print("Your Grade:", grade)
