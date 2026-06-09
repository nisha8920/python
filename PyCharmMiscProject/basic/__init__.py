print("hello world")
#####################(add two number)##############
print("ADD TWO NUMBER :")
a=23
b=45
c=a+b
print(c)
###########(subtract two number)###########
print("SUBTRACT TWO NUMBER :")
a=12
b=10
c=a-b
print(c)
#########(multiple & division two number)##########
print("MULTIPLICATION :")
a=12
b=10
c=a*b
print(c)
print("DIVISION :")
D=12
E=10
f=D/E
print(f)
###############(area of rectangle)##############
print("AREA OF RECTANGLE :")
l=20
b=10
c=l*b
print(c)
##############(area of circle)#########
print("AREA OF CIRCLE :")
r=3
aoc=22/7 * r**2
print(aoc)
################(area of triangle)###########
print("AREA OF TRIANGLE :")
h=12
b=9
aot=1/2*h*b
print(aot)
################(simple interest)###########
print("SIMPLE INTEREST :")
p=2
r=5
t=3
si=p*r*t/100
print(si)
##################(swapping with third variable)###########
print("SWAP WITH THIRD VARIABLE :")
a=3
b=4
c=a
a=b
b=c
print(a)
print(b)
print("SWAP WITHOUT THIRD VARIABLE :")
a=100
b=400
a=a+b
b=a-b
a=a-b
print(a)
print(b)
#############(relational operator)##########
print("ALL RELATIONAL OPERATOR :")
a=29
b=45
c=a+b
p=29
h=40
print("a<b :", a<b)
print("a>b :", a>b)
print("a>=b :", a>=b)
print("a<=b :", a<=b)
print("a==b :", a==b)
print("a!=b :", a!=b)
###################(arithmetic operator)###########
print("ALL ARITHMETIC OPERATOR :")
a=29
b=45
c=a+b
d=a-b
e=a*b
f=a//b
g=a%b
h=a**b
i=a//b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
###################(area of square)##############
print("AREA OF SQUARE :")
s=24
aos=s**2
print(aos)
##################(area of sphere)############
print("AREA OF SPHERE :")
r=8
aos=4*22/7*r**2
print(aos)
#############(volume of sphere)#########
print("VOLUME OF SPHERE :")
r=3
vos=4/3*22/7*r*r*r
print(vos)
############(volume of cylinder)##########
print("VOLUME OF CYLINDER :")
r=6
h=14
voc=22/7*r*r*h
print(voc)
##############(volume of cone)#########
print("VOLUME of cone :")
r=4
h=9
voc=1/3*22/7*r*r*h
print(voc)
############(volume of cube)###########
print("volume of cube :")
s=8
voc=s*s*s
print(voc)
################(volume of cuboid)###########
print("VOLUME OF CUBOID :")
l=4
w=9
h=7
voc=l*w*h
print(voc)
##############(total surface of cuboid)#############
print("TOTAL SURFACE OF CUBOID :")
l=8
b=6
h=5
tsoc=2*(l*b)+(b*h)+(h*l)
print(tsoc)

print("---------------------------------------------------")
a=5
b=10
a=a-1
z=a+b
b=b-1
print(a)
print(b)
print(z)
############## identity operator ##############
print("-------------identity operator--------------")
a=[1,2,3,4,5]
b=a
print(a is not b)
print(a is b)
#############logical operator##########
print("---------logical operator------------")
age = 25
has_license = True
if age >= 18 and has_license:
    print("You are allowed to drive.")
