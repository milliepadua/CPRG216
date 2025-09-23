#premitive data types

x = 2 #int
y = 3.4 #float
z = "Hello" #string
condition = True #Boolean


#Values of an expression or statement
input("Enter your name: ") #it has user input value
#any expression that has a value can be assigned a variable
#hence it should be written as: name = input("Enter your name: ")
age = 2025 - 1990

#Boolean expression
#We are trying to answer a question. The answer is either yes or no (true or false)
#Our answer to this question is the value of the expression
# % = remainder ex. age % 2 == 0 (age divided by 2, remainder equals to 0)

print("is 3>4?", 3>4)
print("is 3<=4?", 3<=4)
print("is 3 equal to 5?", 3==5)
print("is 5>=5?", 5>=5)
print("is age larger than 35?", age>35)
print("are 4 and 5 not equal?", 4!=5)


#IF STATEMENTS
# if (keyword, is a must)
# boolean expression (is a must)
# : is a must
#indentation (must have)
# one or more statements of any type

if 3>4:
    print("yes")
    print("Yes that is true")
print("Outside if statement")


#what is a statement - complete instruction

user_age=int(input("What year were you born?"))
age_comp=int(2025-user_age)
your_age = age_comp>=28

if your_age:
    print("You are a millenial!")
else:
    print("Sorry, you are not in the target age group.")

