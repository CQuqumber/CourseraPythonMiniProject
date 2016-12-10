# template for "Stopwatch: The Game"
import simplegui
# define global variables
time = 0
x = 0
y = 0
flag = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t / 600
    BC = (t-A*600) / 10
    D = (t-A*600) % 10
    if BC < 10 :
        BC = str(0) + str(BC)
    else:
        BC = str(BC)
    return str(A) +" : "+ BC +" . "+ str(D)
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    global flag
    timer.start()
    flag = True
    
def button_stop():
    global x , y , flag
    if flag == True:
        if time % 10 == 0:
            x += 1
        y += 1
    timer.stop()
    flag = False
    
def button_reset():
    global time , x , y
    time = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), [100, 150], 30, 'White')
    canvas.draw_text(str(x)+"/"+str(y), [250, 50], 20, 'red')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 300, 300)
button1 = frame.add_button('Start', button_start, 160)
button2 = frame.add_button('Stop', button_stop, 160)
button3 = frame.add_button('Reset', button_reset, 160)
# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)
# start frame
frame.start()
# Please remember to review the grading rubric
