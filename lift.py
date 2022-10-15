# Calorie calculator for maintenance/bulk/cut
# Outline for calorie calulator -- 
# Enter Name, Age, M/F, Weight, Height
# Find maintenance (BMR)
# Choose bulk/cut
# Maintenance for 2 weeks, +100/weekly for bulk, -100/weekly for cut
print("-------------------------------------------------------------------------------------------------")
print("Step 1: Find your maintenance calories!")
print("-------------------------------------------------------------------------------------------------")
# Using Mifflin St. Jeor formula
#  
#
#
BMR = input("Are you m / f? ")
a = (input("Enter your bodyweight (rounded off) in kgs: "))
b = (input("Enter your height in cms: "))
c = (input("Enter your age in years: "))
d = (input("Do you have a: A. Sedentary life B. Exercise 1-3 days C. Exercise 4-5 days D. Intense exercise 4-5 days E. Intense exercise 6-7 days F. Daily exercise/physical job: [Answer with A/B/C/D/E/F] "))
if d == "A": 
    if BMR == "m": 
      print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300)))
      print()
    elif BMR == "f": 
       print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300)))
       print()
elif d == "B":
    if BMR == "m": 
      print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500)))
      print()
    elif BMR == "f": 
       print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 500)))
       print()
elif d == "C":
    if BMR == "m": 
      print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700)))
      print()
    elif BMR == "f": 
       print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
       print()
elif d == "D":
    if BMR == "m": 
      print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500)))
      print()
    elif BMR == "f": 
       print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
       print()
elif d == "E":
    if BMR == "m": 
      print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700)))
      print()
    elif BMR == "f": 
       print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 900)))
       print()
elif d == "F":
    if BMR == "m":
        print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900)))
        print()
    elif BMR == "f":
        print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 1100)))
        print()
else:
    print("Wrong entry!")
#
# BMI = weight in kgs/height in m sq
#
BMI = float(int(a)/ (float(b)/100)**2)
print(f"Your BMI is {BMI}")
print("-------------------------------------------------------------------------------------------------")
if BMI <= 18.4:
    print("We suggest a bulk programme!")
elif BMI <= 24.9:
    print("We suggest a maintenance based approach or a slight cut if you are skinny fat!")
elif BMI <= 29.9:
    print("Bulking is out of the question. Begin cut.")
else:
    print("Cut.")
    print()
print("-------------------------------------------------------------------------------------------------")
print("Step 2: We made our suggestion which you should consider, but you're in control! Choose your path!")
print("-------------------------------------------------------------------------------------------------")
#
print("Definitions:")
print("1. Bulk - Substantially increase caloric intake so as to increase weight.")
print("2. Cut - A deficit in caloric intake so as to gradually reduce weight")
print("3. Maingain - Continue a maintenance diet with a greater preference for protein")
#
#
# Bulk
# A. Sedentary life -> BMR + 300 + bulk
# B. Exercise 1-3 days -> BMR + 500 + bulk
# C. Execrise 4-5 days -> BMR + 700 + bulk
# D. Intense exercise 4-5 days -> BMR m: + 500 ; f: + 700 + bulk
# E. Intense exercise 6-7 days -> BMR m: + 700 ; f: + 900 + bulk
# F. Daily exercise/physical job -> BMR m: + 900 ; + 1100 + bulk
# add levels i.e., a time frame: beginner in gym (needs recomposition for 2-3 weeks)/ experienced (recomposition for 1 week)
#
prog = input("Would you like to 1. bulk 2. cut 3. maingain? [Answer with 1, 2 or 3] ")
if prog == "1":
    print("Are you a beginner or do you have experience in the gym? [answer with b/e]")
    level = input("Choose level: ")
    if level == "b":
        print("Here is your programme!" )
        if d == "A": # + 300
         if BMR == "m": 
           print("Your count for weeks 1-3 (maintenance) is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 305)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 455)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 555)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 655)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 755)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 855)))
           print()
         elif BMR == "f": 
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 + 155)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 + 255)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 + 355)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 + 455)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 + 555)))
           print()
    elif level == "e":
        if d == "A": # + 300
         if BMR == "m": 
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 + 155)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 + 255)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 + 355)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 + 455)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 + 555)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 + 655)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 + 755)))
           print()
         elif BMR == "f": 
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300 + 155)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300 + 255)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 + 355)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 + 455)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 + 555)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 + 655)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 + 755)))
           print()
    else:
        print("whoops, invalid entry!")
        #
        #
        #
        #
    if level == "b":
        if d == "B": # + 500
         if BMR == "m": 
           print("Your count for weeks 1-3 (maintenance) is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 305 + 200)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 455 + 200)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 555 + 200)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 655 + 200)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 755 + 200)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 855 + 200)))
           print()
         elif BMR == "f": 
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 500)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 + 155)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 + 255)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 + 355)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 + 455)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 + 555)))
           print()
    elif level == "e":
        if d == "B": # + 500
         if BMR == "m": 
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 155)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 255)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 355)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 455)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 555)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 655)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 755)))
           print()
         elif BMR == "f": 
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 500)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 500 + 155)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 500 + 255)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 + 355)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 + 455)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 + 555)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 + 655)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 + 755)))
           print()
    else:
        print("whoops, invalid entry!")
        #
        #
        #
        #
    if level == "b":
        if d == "C": # + 700
         if BMR == "m": 
           print("Your count for weeks 1-3 (maintenance) is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 305 + 400)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 455 + 400)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 555 + 400)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 655 + 400)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 755 + 400)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 855 + 400)))
           print()
         elif BMR == "f": 
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 155)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 255)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 355)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 455)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 555)))
           print()
    elif level == "e":
        if d == "C": # + 700
         if BMR == "m": 
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 155)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 255)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 355)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 455)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 555)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 655)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 755)))
           print()
         elif BMR == "f": 
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 + 155)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 + 255)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 355)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 455)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 555)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 655)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 755)))
           print()
    else:
        print("whoops, invalid entry!")
        #
        #
        #
        #
    if level == "b":
        if d == "D": 
         if BMR == "m": # + 500
           print("Your count for weeks 1-3 (maintenance) is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 305 + 200)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 455 + 200)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 555 + 200)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 655 + 200)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 755 + 200)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 855 + 200)))
           print()
         elif BMR == "f": # + 700
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 155)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 255)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 355)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 455)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 555)))
           print()
    elif level == "e":
        if d == "D": 
         if BMR == "m": # + 500
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 155)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 255)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 355)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 455)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 555)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 655)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 + 755)))
           print()
         elif BMR == "f": # + 700
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 + 155)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 + 255)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 355)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 455)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 555)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 655)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 + 755)))
           print()
    else:
        print("whoops, invalid entry!")
        #
        #
        #
        #
    if level == "b":
        if d == "E": 
         if BMR == "m": # + 700
           print("Your count for weeks 1-3 (maintenance) is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 305 + 400)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 455 + 400)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 555 + 400)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 655 + 400)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 755 + 400)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 855 + 400)))
           print()
         elif BMR == "f": # + 900
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 900)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 155)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 255)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 355)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 455)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 555)))
           print()
    elif level == "e":
        if d == "E": 
         if BMR == "m": # + 700
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 155)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 255)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 355)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 455)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 555)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 655)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 + 755)))
           print()
         elif BMR == "f": # + 900
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 900)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 900 + 155)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 900 + 255)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 355)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 455)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 555)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 655)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 755)))
           print()
    else:
        print("whoops, invalid entry!")
        #
        #
        #
        #
    if level == "b":
     if d == "F": 
        if BMR == "m": # + 900
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 900)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 155)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 255)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 355)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 455)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 + 555)))
           print()
        elif BMR == "f": # + 1100
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 + 155)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 + 255)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 + 355)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 + 455)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 + 555)))
           print()
    elif level == "e":
        if d == "F": 
         if BMR == "m": # + 900
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 + 155)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 + 255)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 + 355)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 + 455)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 + 555)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 + 655)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 + 755)))
           print()
         elif BMR == "f": # + 1100
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100 + 155)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100 + 255)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 + 355)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 + 455)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 + 555)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 + 655)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 + 755)))
           print()
    else:
        print("whoops, invalid entry!")
print("The ideal weight increment should be 0.5 kgs/week. Do not rush.")
#
# Cut
# A. Sedentary life -> BMR + 300 - cut
# B. Exercise 1-3 days -> BMR + 500 - cut
# C. Execrise 4-5 days -> BMR + 700 - cut
# D. Intense exercise 4-5 days -> BMR m: + 500 ; f: + 700 - cut
# E. Intense exercise 6-7 days -> BMR m: + 700 ; f: + 900 - cut
# F. 
#
if prog == "2":
    print("Are you a beginner or do you have experience in the gym? [answer with b/e]")
    level = input("Choose level: ")
    if level == "b":
        print("Here is your programme!" )
        if d == "A": # + 300 - [cut]
         if BMR == "m": 
           print("Your count for weeks 1-3 (maintenance) is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 300)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 300 - 100)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 300 - 150)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 300 - 200)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 300 - 250)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 300 - 300)))
           print()
         elif BMR == "f": 
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 - 50)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 - 100)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 - 150)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 - 200)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 300 - 250)))
           print()
    elif level == "e":
        if d == "A": # + 300 - [cut]
         if BMR == "m": 
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 - 100)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 - 150)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 - 200)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 - 250)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 - 300)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 - 350)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300 - 400)))
           print()
         elif BMR == "f": 
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300 - 50)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300 - 100)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300 - 150)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300 - 200)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300 - 250)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300 - 300)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300 - 350)))
           print()
    else:
        print("whoops, invalid entry!")
        #
        #
        #
        #
    if level == "b":
        if d == "B": # + 500 - [cut]
         if BMR == "m": 
           print("Your count for weeks 1-3 (maintenance) is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 500)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 500 - 100)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 500 - 150)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 500 - 200)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 500 - 250)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 500 - 300)))
           print()
         elif BMR == "f": 
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 500)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 - 50)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 - 100)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 - 150)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 - 200)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 - 250)))
           print()
    elif level == "e":
        if d == "B": # + 500
         if BMR == "m": 
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 100)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 150)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 200 )))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 250)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 300)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 350)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 400)))
           print()
         elif BMR == "f": 
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 500)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 500 - 50)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 500 - 100)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 - 150)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 - 200)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 - 250)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 - 300)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 500 - 350)))
           print()
    else:
        print("whoops, invalid entry!")
        #
        #
        #
        #
    if level == "b":
        if d == "C": # + 700 - [cut]
         if BMR == "m": 
           print("Your count for weeks 1-3 (maintenance) is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 700)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 700 - 100)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 700 - 150)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 700 - 200)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 700 - 250)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 700 - 300)))
           print()
         elif BMR == "f": 
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 50)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 100)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 150)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 200)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 250)))
           print()
    elif level == "e":
        if d == "C": # + 700 - [cut]
         if BMR == "m": 
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 100)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 150)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 200)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 250)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 300)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 350)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 400)))
           print()
         elif BMR == "f": 
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 - 50)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 - 100)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 150)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 200)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 250)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 300)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 350)))
           print()
    else:
        print("whoops, invalid entry!")
        #
        #
        #
        #
    if level == "b":
        if d == "D": 
         if BMR == "m": # + 500 - [cut]
           print("Your count for weeks 1-3 (maintenance) is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 500)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 500 - 100)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 500 - 150)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 500 - 200)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 500 - 250)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 500 - 300)))
           print()
         elif BMR == "f": # + 700 - [cut]
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 50)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 100)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 150)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 200)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 700 - 250)))
           print()
    elif level == "e":
        if d == "D": 
         if BMR == "m": # + 500 - [cut]
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 100)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 150)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 200)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 250)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 300)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 350)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500 - 400)))
           print()
         elif BMR == "f": # + 700 - [cut]
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 - 50)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 - 100)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 - 150)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 - 200)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 - 250)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 - 300)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700 - 350)))
           print()
    else:
        print("whoops, invalid entry!")
        #
        #
        #
        #
    if level == "b":
        if d == "E": 
         if BMR == "m": # + 700
           print("Your count for weeks 1-3 (maintenance) is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 700)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 700 - 100)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 700 - 150)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 700 - 200)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 700 - 250)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 700 - 300)))
           print()
         elif BMR == "f": # + 900
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 900)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 - 50)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 - 100)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 - 150)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 - 200)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 - 250)))
           print()
    elif level == "e":
        if d == "E": 
         if BMR == "m": # + 700
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 100)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 150)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 200)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 250)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 300)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 350)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700 - 400)))
           print()
         elif BMR == "f": # + 900
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 900)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 900 - 50)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 900 - 100)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 - 150)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 - 200)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 - 250)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 - 300)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 900 - 350)))
           print()
    else:
        print("whoops, invalid entry!")
        #
        #
        #
        #
    if level == "b":
     if d == "F": 
        if BMR == "m": # + 900 - [cut]
           print("Your count for weeks 1-3 (maintenance) is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 900)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 900 - 100)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 900 - 150)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 900 - 200)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 900 - 250)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 900 - 300)))
           print()
        elif BMR == "f": # + 1100 - [cut]
           print("Your count for weeks 1-3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 - 50)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 - 100)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 - 150)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 - 200)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c)  - 161 + 1100 - 250)))
           print()
    elif level == "e":
        if d == "F": 
         if BMR == "m": # + 900 - [cut]
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 - 100)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 - 150)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 - 200)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 - 250)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 - 250)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 - 300)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900 - 350)))
           print()
         elif BMR == "f": # + 1100 - [cut]
           print("Your count for week 1 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100)))
           print("Your count for week 2 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100 - 50)))
           print("Your count for week 3 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100 - 100)))
           print("Your count for week 4 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100 - 150)))
           print("Your count for week 5 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100 - 200)))
           print("Your count for week 6 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100 - 250)))
           print("Your count for week 7 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100 - 300)))
           print("Your count for week 8 is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 1100 - 350)))
           print()
    else:
        print("whoops, invalid entry!")
        #
        #
        #
        #
    print("The ideal amount of weight to lose per week is 0.5 kgs. Do not rush.")
if prog == "3":
   print("Are you a beginner or do you have experience in the gym? [answer with b/e]")
   level = input("Choose level: ")
   if level == "b":
      print("Here is your programme!")
      if d == "A": 
         if BMR == "m": 
           print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300)))
           print()
         elif BMR == "f": 
          print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300)))
          print()
      elif d == "B":
         if BMR == "m": 
           print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500)))
           print()
         elif BMR == "f": 
          print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 500)))
          print()
      elif d == "C":
        if BMR == "m": 
          print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700)))
          print()
        elif BMR == "f": 
          print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
          print()
      elif d == "D":
        if BMR == "m": 
          print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500)))
          print()
        elif BMR == "f": 
          print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
          print()
      elif d == "E":
       if BMR == "m": 
        print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700)))
        print()
      elif BMR == "f": 
         print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 900)))
         print()
      elif d == "F":
       if BMR == "m":
         print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900)))
         print()
      elif BMR == "f":
        print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 1100)))
        print()
      else:
        print("Wrong entry!")
   if level == "e":
     if d == "A": 
         if BMR == "m": 
           print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 300)))
           print()
         elif BMR == "f": 
          print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 300)))
         print()
     elif d == "B":
         if BMR == "m": 
          print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500)))
          print()
         elif BMR == "f": 
          print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 500)))
         print()
     elif d == "C":
        if BMR == "m": 
          print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700)))
          print()
        elif BMR == "f": 
         print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
         print()
     elif d == "D":
        if BMR == "m": 
         print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 500)))
         print()
        elif BMR == "f": 
         print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 700)))
         print()
     elif d == "E":
       if BMR == "m": 
        print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 700)))
        print()
       elif BMR == "f": 
        print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) - 161 + 900)))
       print()
     elif d == "F":
       if BMR == "m":
        print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 900)))
        print()
       elif BMR == "f":
        print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c) + 5 + 1100)))
       print()
print()