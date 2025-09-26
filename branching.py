#premitive data types

'''x = 2 #int
y = 3.4 #float
z = "Hello" #string
condition = True #Boolean'''


#Values of an expression or statement
#input("Enter your name: ") #it has user input value
#any expression that has a value can be assigned a variable
#hence it should be written as: name = input("Enter your name: ")
'''age = 2025 - 1990'''

#Boolean expression
#We are trying to answer a question. The answer is either yes or no (true or false)
#Our answer to this question is the value of the expression
# % = remainder ex. age % 2 == 0 (age divided by 2, remainder equals to 0)

'''print("is 3>4?", 3>4)
print("is 3<=4?", 3<=4)
print("is 3 equal to 5?", 3==5)
print("is 5>=5?", 5>=5)
print("is age larger than 35?", age>35)
print("are 4 and 5 not equal?", 4!=5)'''


#IF STATEMENTS
# if (keyword, is a must)
# boolean expression (is a must)
# : is a must
#indentation (must have)
# one or more statements of any type:
    #elif (optional)
    #condition (mandatory for elif) and : + indentation
    #one or more statements
#non indented else (optional)
# : is a must after else
#indented
#one or more statements (is a must)
#elif = else if

'''if 3>4:
    print("yes")
    print("Yes that is true")
print("Outside if statement")'''


#what is a statement - complete instruction

'''user_age=int(input("What year were you born?"))
age_comp=2025-user_age
your_age = age_comp>=28

if your_age:
    print("You are a millenial!")
else:
    print("Sorry, you are not in the target age group.")'''

"""print("Welcome to the grade system")
grade=int(input("Please Enter your grade"))

if grade >= 90:
    letter_grade ='A'
elif grade>=80:
    letter_grade = 'B'
elif grade>=70:
    letter_grade = 'C'
elif grade>=60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("Your letter grade is ", letter_grade)"""

'''
read a,b, and c from the user
if a == 0, then x1 = x2 =-c/b
else
    if 4*a*c < b^2 then
    x1 = (-b +sqrt(b^2 - 4*a*c))/(2*a)
    x2 = (-b -sqrt(b^2 - 4*a*c))/(2*a)
    else
        print "No possible solution"
        exit
    print x1, x2

    end

'''

a = (float(input("Enter first number: ")))
b = (float(input("Enter second number: ")))
c = (float(input("Enter third number: ")))

x1 = (-b + sqrt((b^2) - (4*a*c))/(2*a)
x2 = (-b - sqrt((b^2) - (4*a*c))/(2*a)

if a == 0:
    x1 = -b/c
    x2 = -b/c
else:
    if b**2 >= 4*a*c:
        x1 = (-b + ((b**2) - (4*a*c)) ** 0.5/(2*a)
        x2 = (-b - ((b**2) - (4*a*c)) ** 0.5/(2*a)
    else:
        x1 = None
        x2 = None
    print("No possible solution")
print(x1,x2)