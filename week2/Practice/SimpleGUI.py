# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter = 0
# Define "helper" functions
def increament():
    global counter
    counter += 1
# Define event handler functions
def tick():
    increament()
    print counter

def buttonpress():
	global counter
	counter = 0
# Create a frame
frame = simplegui.create_frame('Testing', 200, 200, 300)
# Register event handlers
timer = simplegui.create_timer(1000,tick)
frame.add_button("Click me !", buttonpress)
# Start frame and timers
frame.start()
timer.start()
