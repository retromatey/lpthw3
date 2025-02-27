my_name = 'Jason Tennant'
my_age = 44
my_height = 76.0
my_weight = 200.0
my_eyes = 'hazel'
my_teeth = 'White'
my_hair = 'Brown'

# Write some variables to convert the inches and pounds to centimeters and
# kilograms.
my_weight_kg = my_weight * 0.4536
my_height_cm = my_height * 2.54

print(f"Let's talk about {my_name}.")
print(f"He's {my_height_cm} centimeters tall.")
print(f"He's {my_weight_kg} kilograms heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the tea.")

total = my_age + my_height_cm + my_weight_kg
print(f"If I add {my_age}, {my_height_cm}, and {my_weight_kg} I get {total}.")
