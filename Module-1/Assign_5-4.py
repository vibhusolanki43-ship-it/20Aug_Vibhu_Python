'''rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1): 
    for j in range(1, i + 1):  
        print("*", end=" ")   
    print()'''

def print_star_pattern(rows):

    for i in range(1, rows + 1):
        num_spaces = rows - i
        num_stars = i
        row_output = (' ' * num_spaces) + ('* ' * num_stars).strip()
        print(row_output)

NUMBER_OF_ROWS = 5

print_star_pattern(NUMBER_OF_ROWS)

