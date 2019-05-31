import turtle

color1 = "#0000ff"
color2 = "#00ff00"
colorToggle = 0

def setUp():
	turtle.penup()
	turtle.goto(-750,375)
	turtle.speed(1)
	turtle.shape("turtle")

def square(length):
	rectangle(length, length)

def filledSquare(length):
	turtle.begin_fill;
	square(length)
	turtle.end_fill;
	
def rectangle(length, width):
	for i in range(2):
		turtle.forward(length)
		turtle.right(90)
		turtle.forward(width)
		turtle.right(90)

def filledRectangle(length, width):
	turtle.begin_fill;
	rectangle(length, width)
	turtle.end_fill;
	
def toggleSetUp(setColor1, setColor2):
	global color1
	global color2
	color1 = setColor1
	color2 = setColor2
	
def toggleColor():
	global colorToggle
	global color1
	global color2
	
	if colorToggle == 0:
		turtle.color(color1)
		colorToggle = 1
	else:
		turtle.color(color2)
		colorToggle = 0
