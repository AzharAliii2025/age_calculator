import datetime

# Get the current year
current_year = datetime.datetime.now().year

# Ask user for their birth year
birth_year = input("Enter your birth year (e.g. 2000): ")

# Check if input is numeric
if birth_year.isdigit():
    birth_year = int(birth_year)
    age = current_year - birth_year

    # Validate age range
    if 0 < age < 130:
        print(f"You are {age} years old.")
    else:
        print("That doesn't seem like a valid age.")
else:
    print("Please enter a valid year in digits.")
