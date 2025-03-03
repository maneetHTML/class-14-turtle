import turtle
ns=int(input("enter the number of side :"))
l=int(input("enter the length :"))
angle=360/ns
mywindow=turtle.Screen()
mywindow.bgcolor("lightgreen")
mypen=turtle.Turtle()
for i in range(ns):
    mypen.fd(l)
    mypen.left(angle)
turtle.done()