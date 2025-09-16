#I want to compute the circumfererence and the area of the circle
#assume the circle radius is 5
#and that pi is 3.14


radius = 5
pi = 3.14
circum = 2 * (pi * radius)
area = pi * (radius * radius)

print("The circumference of the circle is ", circum)
print("The area of the circle is ", area)

#static type vs dynamic type
#int main() {
    #int x; #or float x
   # x = 4;
    #x = 4.3;
   # x = "hello";

#print ("Hello!"/n)
#}

#constant - special type of variable whose value cannot be changed

from typing import Final
r = 5


#casting

x = 3/4 #int
y = 4 #int
z = x/y #float, automatic casting

print(x)

#manual casting or explicit casting
int(z)
print(int(z))
print(int("43"))
print(str(43))

x = 1
print(x, type(x))

y = float(x) #int to float = promotion

print(y, type(y))

v = 4.3
print(v, type(v))
u = int(v)
print(u, type (u))


#print = prints to screen, "output"
#input = entry

pi = 3.14
user_input = input("Please enter the radius of the circle: ")
r = int(user_input)
circum = 2 * pi * r
print(circum)
