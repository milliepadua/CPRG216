#Week 3 

'''4 assignment statements for int, float, boolean, string
print the variables with type



x = 7
y = 5.2
z = True
u = "software"

print(x,type(x))
print(y,type(y))
print(z,type(z))
print(u,type(u))

print("The value of x is: ",x, "and the class type is: ", type(x))
print("The value of y is: ",y,"and the class type is: ",type(y))
print("The value of z is: ",z,"and the class type is: ",type(z))
print("The value of u is: ",u,"and the class type is: ",type(u))

num_as_text="43"
num_as_num=int(num_as_text)

print(num_as_text)
print(num_as_num)
print(str(num_as_num)) #equivalent
print(num_as_num*2)

num = 3
num_f = float(3)

num2 = 3.4
num2_i = int(num2)

num2_as_text = str(num2)

#if you put any variable in the context of a string - automatically it will be a string

#Using input function, note that input function always return a string (text)

#year_of_birth = input("Please enter your year of birth\n")

#print("Your age is ", 2025 - int(year_of_birth))
'''

'''
#create a program, add input from user, and do a calculation
'''

#weight_in_kg = int(input("Please enter your weight in Kilograms: "))
#weight_in_lbs = weight_in_kg * 2.2

#print("Your weight in pounds is: ", weight_in_lbs)


'''
print function
    prints the values to a stream
    working with a separator
'''

print("Hello", "world", sep=' ', end=' ')
print("Hello", "world", sep=' ')
print("Hello\tworld")
print("Hello\nworld")

#without separator, it will be a space. This is especially important if you are using ms excel or other tables
#if you want to combine them together without the space, sep='' ; if you want to add comma , sep=','
#end : by default: \n <- means next line ; can also add in message  
# \t = tab
# \m = 
#to print a single quote in a text: add \'
#ex. print("What is the student\'s name?") or print('What is the student\'s name?')
#to print or include a \ in the text, add another \. example: print('Use this symbol \\ to make an escape character')


'''
Exercise 2.1

Write a program with two inputs, current price and last month's price (both integers). Then, output a summary listing the price, the change since last month,
and the estimated 


'''

'''
lifecycle:



algorithm
-flowchart and pseudocode
-if statement and formula


function call:
print
int (integer) - casting (implicit vs explicit)


'''