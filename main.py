from graphics.Dgraphics.sphere import *
from graphics.rectangle import *
from graphics.circle import *
from graphics.Dgraphics.cuboid import *

print("rectangle")
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))

print("circle")
radius=int(input("enter the radius:"))

print("cuboid")
lc=int(input("enter the length:"))
wc=int(input("enter the width:"))
hc=int(input("enter the height"))
print("sphere")
spr=int(input("enter the radius of sphere:"))


a=area(l,b)
p=perimeter(l,b)
ca=cirarea(radius)
cp=cirperimeter(radius)
cua=cuboidarea(lc,wc,hc)
cup=cuboidperimeter(lc,wc,hc)
spar=sparea(spr)
spvo=spvolume(spr)


print("Area  of rectangle is :",a)
print("perimeter  of rectangle is :",p)
print("area of circle :",ca)
print("perimeter of circle",cp)
print("area of cuboid:",cua)
print("perimeter of cuboid",cup)
print("area of sphere:",spar)
print("volume of sphere:",spvo)
