text = "  Python Programming is Fun!  "
print("Original string:", repr(text))

# uppercase
upper_text = text.upper()
print("Uppercase:", upper_text)

#Clowercase
lower_text = text.lower()
print("Lowercase:", lower_text)

#Remove leading and trailing spaces
stripped_text = text.strip()
print("Stripped:", repr(stripped_text))

# Replace a word
replaced_text = text.replace("Fun", "Awesome")
print("Replaced 'Fun' with 'Awesome':", replaced_text)

#split
words = text.split()
print("Split into words:", words)

#Check if string ends with 'Fun!'
ends = text.strip().endswith("Fun!")
print("Ends with 'Fun!'?:", ends)

#Capitalize 
capitalized = text.strip().capitalize()
print("Capitalized:", capitalized)
