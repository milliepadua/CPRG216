'''
1- read a, b, and c from the user
2- if a == 0 then x1 = x2 = -c/b

    else
        if 4*a*c < b^ 2 then
        x1 = (-b + sqrt(b^2 - 4 * a * c)) / (2*a) **0.5
        x2 = (-b - sqrt(b^2 - 4 * a * c)) / (2*a) **0.5 

        else
            print "No possible solution"
            exit
    
    print x1, x2

'''

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))


'''if a == 0:
    x2 = x1
elif 4*a*c <= b*b:
    x1 = (-b +((b**2 - 4*a*c))**.05) / (2*a)
    x2 = (-b -((b**2 - 4*a*c))**.05) / (2*a)
else:
    print("No possible solution")

print(x1, x2)
'''
'''
if 4*a*c <= b**2:
    x1 = (-b +((b**2 - 4*a*c))**.05) / (2*a)
    x2 = (-b -((b**2 - 4*a*c))**.05) / (2*a)
elif a == 0:
    x1 = -c/b
    x2 = x1   
else:
    print("No possible solution")
print(x1, x2)
'''

if a==0:
    x1 = -c/b
elif 4*a*c <= b**2:
    x1 = int((-b +((b**2 - 4*a*c))**.05) / (2*a))
    x2 = int((-b -((b**2 - 4*a*c))**.05) / (2*a))
else:
    print("No possible solution")
x2 = x1

print(x1,x2)



