# Calorie calculator for maintenance/bulk/cut
# Outline for calorie calulator -- 
# Enter Name, Age, M/F, Weight, Height
# Find maintenance (BMR)
# Choose bulk/cut
# Maintenance for 2 weeks, +100/weekly for bulk, -100/weekly for cut


def fitness_program():
    def calculate_maintenance(gender, weight, height, age, activity_multiplier):
        bmr = 10 * weight + (6.25 * height) - (5 * age) + (5 if gender == "m" else -161)
        return bmr + activity_multiplier

    activity_multipliers = {
        "A": 300,
        "B": 500,
        "C": 700,
        "D": {"m": 500, "f": 700},
        "E": {"m": 700, "f": 900},
        "F": {"m": 900, "f": 1100}
    }

    print("Step 1: Find your maintenance calories!")
    gender = input("Are you m / f? ").lower()
    weight = int(input("Enter your bodyweight (rounded off) in kgs: "))
    height = float(input("Enter your height in cms: "))
    age = int(input("Enter your age in years: "))
    activity_level = input("Do you have a: A. Sedentary life B. Exercise 1-3 days C. Exercise 4-5 days D. Intense exercise 4-5 days E. Intense exercise 6-7 days F. Daily exercise/physical job: [Answer with A/B/C/D/E/F] ").upper()

    if activity_level in activity_multipliers:
        multiplier = activity_multipliers[activity_level]
        if isinstance(multiplier, dict):
            multiplier = multiplier[gender]
        maintenance = calculate_maintenance(gender, weight, height, age, multiplier)
        print(f"Your maintenance is: {maintenance}")
    else:
        print("Wrong entry!")

    BMI = weight / (height / 100)**2
    print(f"Your BMI is {BMI}")

    if BMI <= 18.4:
        print("We suggest a bulk programme!")
    elif BMI <= 24.9:
        print("We suggest a maintenance based approach or a slight cut if you are skinny fat!")
    elif BMI <= 29.9:
        print("Bulking is out of the question. Begin cut.")
    else:
        print("Cut.")

    print("Step 2: We made our suggestion which you should consider, but you're in control! Choose your path!")
    prog = input("Would you like to 1. bulk 2. cut 3. maintain? [Answer with 1, 2 or 3] ")

    if prog == "1":
        level = input("Are you a beginner or do you have experience in the gym? [answer with b/e] ")
        weeks = 8 if level == "b" else 6
        bulk_increment = 150

        for week in range(1, weeks + 1):
            if week <= 2 or level == "b" and week <= 3:
                print(f"Your count for week {week} is: {maintenance}")
            else:
                maintenance += bulk_increment
                print(f"Your count for week {week} is: {maintenance}")
    elif prog == "2":
        level = input("Are you a beginner or do you have experience in the gym? [answer with b/e] ")

        if level not in ("b", "e"):
            print("Whoops, invalid entry!")
        else:
            print("Here is your programme!")
            base_cuts = {"A": 300}
            additional_cuts = [0, 100, 150, 200, 250, 300, 350, 400]
        for week, cut in enumerate(additional_cuts, start=1):
            if activity_level in base_cuts:
                base = base_cuts[activity_level]
                count = maintenance - base - cut

                if level == "b" and week <= 3 or level == "e":
                    print(f"Your count for week {week} is: {count}")
            print()
    elif prog == "3":
        level = input("Are you a beginner or do you have experience in the gym? [answer with b/e] ")
        if level not in ("b", "e"):
          print("Whoops, invalid entry!")
        else:
          print("Here is your programme!")
        for week in range(1, 9):
            print(f"Your count for week {week} is: {maintenance}")
            print()
    else:
      print("Wrong entry!")
print()
fitness_program()