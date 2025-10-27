import random
rand_int = random.randint(1, 10)
rand_float = random.random()
rand_range = random.randrange(5, 20, 2)  
colors = ["Red", "Green", "Blue", "Yellow"]
rand_choice = random.choice(colors)

random.shuffle(colors)

print(f"Random integer between 1 and 10: {rand_int}")
print(f"Random float between 0 and 1: {rand_float}")
print(f"Random number from range 5-20 (step 2): {rand_range}")
print(f"Random choice from list: {rand_choice}")
print(f"Shuffled list: {colors}")
