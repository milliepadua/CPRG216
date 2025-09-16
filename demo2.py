x = 5 # assignment statement
print(x) #function call


#variables
    #variable has a name
    #has a value
    #has an address
    #has a size
    #has a type (int (<- not a decimal), float)

i = 3 #int integer
f = 4.5 #float (decimal)
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
d_ = 3//4 #floor division; smaller value
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
