weight = float(input("Enter your weight: ")) 
weight_in_lbs = weight * 2.20462
weight_in_kg = weight / 2.20462
kg_lbs = input("Is your weight in (K)g or (L)bs? ").strip().upper()

if kg_lbs == 'K':
    print(weight_in_kg)
elif kg_lbs == 'L':
    print(weight_in_lbs)
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")

# Output will depend on the input provided by the user.

