x = 5 # assignment statement
print(x) #function call


#variables
    #variable has a name
    #has a value
    #has an address
    #has a size
    #has a type (int (<- not a decimal), float)

i = 3 #int integer (4 bytes)
f = 4.5 #float (decimal) (8 bytes)
b = True #boolean Boole
s = "hello" #string - letters; uses double quotes
msg = 'Hello World!' #single quotes are for single words
ch = 'a' #this is still a string (character)


print(i, type(i))
print(f, type(f))
print(s, type(s))
print(msg, type(msg))
print(b, type(b))
print(ch, type(ch))

#variable names can use letters, digits, and underscore only (you can't have a comma in name)
#it can't start with a number
#can't start with _ but you shouldn't use it (because it has a different meaning) "privacy"
#use meaningful variable names (if there are two words, use underscore as "space, eg, circle_radius")

circle_radius = 5
PI = 3.14
circle_radius = 7 #reassignment
area_of_circle = PI * circle_radius * circle_radius

print("The area of the circle is: ", area_of_circle)


#naming convention
#Operations:

a = 3+4
b = 4-3
c = 4*3
d = 3/4
d_ = 3//4 #floor division; smaller value; round up the answer
e = 4%3 #the result is the remainder after division
f = 3**2 #exponent

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(d_, type(d_))
print(e, type(e))
print(f, type(f))

#combining variables
e = a+b #process the assignment from right to left
#it means evaluate a+b first, then add the result to the variable

print("The value of e is ", e)




#18 September 2025

#git config user.name
#git init
#git status - which branch you are on and the files not yet committed
#git add filename or git add * (for all)
#git commit -m (always add message)
#git push (add origin / main (branch - cloud -mirror))
#git lab, git hub, etc (repositories)

#smallest element in a program - statement
#-> complete instruction to the computer
#assignment statement = allocates a memory in the computer and has a name, value
'''#function call:
#v -4.3 
#print(v, type(v))
'''

#add comment (single line)
'''
comments - multiline (''' ''')
'''



#This is our class 3 (single line comment)
'''
multiline comment
'''

'''
primitive - included in the language
eg python: int, boolean, string, float
string - an array of text (also in C)
arguments are comma separated

print - sends any command into the output string

casting - changing the type (eg from int to float)/ promoting or demoting
explicit casting - 
uses the type as the command / 

some functions call: print, input, int, float, str, bool

string to int
eg
num_as_text="43"
num_as_num=int(num_as_text)

#if you put any variable in the context of a string - automatically it will be a string

#Using input function, note that input function always return a string (text)

#year_of_birth = int(input("Please enter your year of birth\n"))
# can also write:  print("Your age is ", 2025 - int(year_of_birth)) without adding int in input line
#create a program, add input from user, and do a calculation


weight_in_kg = int(input("Please enter your weight in Kilograms: "))
weight_in_lbs = round(weight_in_kg * 2.2,2) #no need to add round for now to round off numbers




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
precedence rules


expression = 3+4*0-300+12/3
the answer is a float because of division

expression = 4/2*3
if they have the same rank (multiplication and division, addition and subtraction), start from left to right




More about assignment
-> reads from right to left (eg x = 5, where you tell the computer to assign 5 to x)

'''


expression = 3+4*0-300+12/3
print(expression)

expression = 4/2*3
print(expression)

x = 3
x = x + 5

print(x)

'''
#can we have a shorthand for this expression?
# x += 5 (same as x = x + 5)
# other expressions:

x -= 2 (same as x = x - 3 )
x *= 3 (same as x = x * 3)
x /= 2 (same as x = x / 2)
x **= 4 (same as x = x ** 4)
'''

x += 5
print (x)

x -= 2
print (x)

x *= 3
print (x)

x /= 2
print (x)

x **= 4
print (x)


'''
special value of 1

x += 1 # x = x+1
'''