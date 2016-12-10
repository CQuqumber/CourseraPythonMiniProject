import simplegui

x = 0

def f(n) :
	return  n**x

def button_handler( ):
	global x
	x += 1

def input_handler(text) :
	print f( float( text ) )

frame = simplegui.create_frame("Example", 200 ,200)
frame.add_button("Increment", button_handler)
frame.add_input("Number:", input_handler, 100)

frame.start()

