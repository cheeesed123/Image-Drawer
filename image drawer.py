import turtle
import sys
# a = "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRBBBBBRRRRRRRRRRBRRRRRRBRRRRRRRBRRRRRRRRBRRRRRBRRRRRRRRRRRRRRBRRRRRRRRRRRRRRBRRRRRRRRRRRRRRRBRRRRRRRRRRRRRRRBRRRRRRRRRRRRRRRRBRRRRRRRRRRRRRRRRBRRRRRRRRRRRRRRRRBRRRRRRRRRRRRRRRRBRRRRRRRRRRRRRRRRBBBBBRRRRRRRRRRRRRRRRRRRR"
print("Key:", "R: Red", "B: Black", "G: Green", "O: Orange", "P: Pink", "L: Blue", "Y: Yellow", "U: Purple", "W: White", sep="\n")
width = int(input("Enter Width (integer):"))
pixel_size = int(input("Pixel Size (integer) (default is 10):"))
a = input("Enter list data:")
item = ""
inputs = []
count = int(-1)
row = 0
width_number = 0
width_number_list = []
while count < ((len(a) - 1) // width):
    count += 1
    width_number += width
    width_number_list.append(width_number)
# counting width_numbers
for item in a:
    inputs.append(item)
# adding colors to list
count = 0
# while count < len(inputs):
#    if inputs[count] is "R":
#        del inputs[count]
#        inputs.insert(count, "B")
#    else:
#        del inputs[count]
#        inputs.insert(count, "R")
#    count += 1
# switching colors
turtle.color("white")
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(475)
turtle.right(180)
# positioning
item = 0
count = 0
while item < len(inputs):
    if inputs[item] in ["R", "r"]:
        turtle.color("red")
    elif inputs[item] in ["B", "b"]:
        turtle.color("black")
    elif inputs[item] in ["G", "g"]:
        turtle.color("green")
    elif inputs[item] in ["O", "o"]:
        turtle.color("orange")
    elif inputs[item] in ["P", "p"]:
        turtle.color("pink")
    elif inputs[item] in ["L", "l"]:
        turtle.color("blue")
    elif inputs[item] in ["Y", "y"]:
        turtle.color("yellow")
    elif inputs[item] in ["U", "u"]:
        turtle.color("purple")
    elif inputs[item] in ["W", "w"]:
        turtle.color("white")
    else:
        print("Error! Color not recognized.")
        sys.kill()
    # set color
    turtle.begin_fill()
    count = 0
    while count <= 4:
        turtle.forward(pixel_size)
        turtle.right(90)
        count += 1
    # make square
    turtle.end_fill()
    turtle.left(90)
    item += 1
    if item in width_number_list:
        turtle.setheading(270)
        turtle.forward(pixel_size)
        turtle.setheading(0)
        turtle.backward((width * pixel_size))
        row += 1
    print("Square:", item, "Line:", row)
# draw squares
turtle.exitonclick()