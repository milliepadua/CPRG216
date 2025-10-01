'''
"coding is what you have, but you have to stick to rules"

if + boolean statement (true or false)

if True:
    print("Condition is True")
    *can have as many conditions as you want
elif x>0: *elif is used if there are more conditions to be met
    print("x is positive")
elif x<0: 
    print("x is negative")

else:
    print("Condition is False")

*used to validate inputs / check    


I have 5 instructors teaching some courses
Hani - CPRG216 -I 2025 Fall
John - CPRG215 -A 2025 Fall
Mary - CPRG216 -I 2025 Winter
Sam - CPRG216 -I 2024 Fall

combining logical expressions:
-and
-or


NOT:
x - x1
0 - 1
1 - 0


check truth table


'''

print("Welcome to instructor selector software.")

code = input("Please enter the course code: ")
season = input("Please enter the season (Fall, Winter, Summer): ")
year = int(input("Please enter the year (e.g., 2024): "))
section = input("Please enter the section (A, B, C, I): ")

instructor = "Not Found"

if code == "CPRG216" and section == "I":
    if season == "Fall" and year == 2025:
        instructor = "Hani"
    elif season == "Fall" and year == 2025:
        instructor = "Hani"
    elif season == "Winter" and year == 2025:
        instructor = "Hani"  
    elif season == "Fall" and year == 2025:
        instructor = "Hani"  
elif code == "CPRG215" and section == "A"
    if season == "Fall" and year == 2025:
        instructor = "John"
    else:
        instructor = "Not Found"


#combining logical expressions