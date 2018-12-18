import turtle

def setUp():
	turtle.penup()
	turtle.goto(-750,375)
	turtle.speed(1)
	turtle.shape("turtle")

def square(length):
	for i in range(4):
	turtle.forward(length)
		turtle.right(90)

def filledSquare(length):
	turtle.begin_fill;
	square(94)
	turtle.end_fill;
