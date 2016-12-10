import simplegui
import time
interval = 0
D = 0
x = 0
y = 0
t = "0:00.0"
ratio = "x/y"
height = 300
weight = 300
def tick():
    global interval ,t ,ratio
    if interval == 0:
        timer.stop()
    else:
        timer.start()
    t = format(interval)
    interval += 1 
    print interval
      
    
    
def format(time):   
    global D, interval
    if interval > 6000: #10 Minutes Limited
        timer_reset()
        return "10:00.0"
    
    else: # Time Converter
        if time/600 == 0:
            A = time/600
            B = time/100
            C = (time - B*100)/10
            D = (time - B*100 - C*10)
            return str(A)+":"+str(B)+str(C)+"."+str(D)       
        else:
            A = time/600
            B = (time-600*A)/100
            C = ((time-600*A) - B*100)/10
            D = ((time-600*A) - B*100 - C*10)
            return str(A)+":"+str(B)+str(C)+"."+str(D) 

    
def draw_handler(canvas):
    canvas.draw_text(t, [100,150], 48, "silver")
    canvas.draw_text(ratio, [height*0.75,weight*0.15], 36, "green")    
    
 
    
def timer_start(): 
    timer.start()
 
    
def timer_stop():
    timer.stop()
    global ratio, interval,x ,y, D
    if D == 0: #
        x += 1
        y += 1
        ratio = str(x)+"/"+str(y)
        return ratio
    elif D != 0:
        y += 1
        ratio = str(x)+"/"+str(y)
        return ratio

    
def timer_reset():
    global interval,x,y,ratio
    interval = 0
    x = 0
    y = 0
    ratio = "x/y"
    timer.stop()
    tick()
    

 

frame = simplegui.create_frame("StopWatch", height, weight)
timer = simplegui.create_timer(100, tick)

frame.add_button('Start', timer_start,60)
frame.add_button('Stop', timer_stop,70)
frame.add_button('Reset', timer_reset,80)

frame.set_draw_handler(draw_handler)

frame.start()
 
timer.start()