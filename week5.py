"""
Review of if statement

"""

'''age = 18

if age >= 18:
    print("You are allowed to be in the party")
else:
    print("Sorry kid")'''


#While Loop:

'''
-while (mandatory)
-condition (True or false; mandatory)
-the colon: (mandatory)
-one or more statement - indented

ex
while condition:
    statement 1
    statement 2
    ...
'''

#True all the time

#boolean naming convention - should be in a form of question such as is_adult
'''
while True:
    print("I am running...")
    #will keep on running until you press CTRL+C or CTRL+X'''

'''while False:
    print("I am not running...")'''


age = 19
is_adult = age >= 18

while is_adult:
    print("The user is adult")
    age = 17
    is_adult = age >= 18

#example print numbers from 1 to 10

'''number = 0

while number < 10:
    #number = number + 1 #augmented operator
    number += 1
    print(number)'''

#or

'''number = 11

while number > 1:
    number -= 1
    print(number)'''


number = 0
sum = 0

while number < 100:
    number += 1
    sum += number
print(sum) #if not indented under while, means it will perform this action once statement is false

'''
while number < 100:
    number + 1 # increment the number
    sum + number
    print (sum)
'''

'''
pseudocode:
1. start with number = 0
sum = 0

2. increase number by 1
3. add number to sum
*2 and 3 to be repeated

4. repeat steps 2,3,4 till number = 100 #if seen in pseudocode, this is a while loop or for statement

Gaus: n(n+1) / 2
sum = (100*(100+1))/2
'''

#factorial
number = 0
product = 1 #anything multiplied by 1 is itself - neutral number

while number < 10:
    number += 1
    product *= number
print(product)


