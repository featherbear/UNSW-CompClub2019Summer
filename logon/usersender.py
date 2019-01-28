from microbit import *

id = 0
def nextID():
    global id
    id = (id+1) % 41

def updateScreen():
    global id
    display.clear()
    if id == 0:
        display.show("0")
        return
    if id >= 40:
        display.set_pixel(0,1,9)
    if id >= 30:
        display.set_pixel(0,2,9)
    if id >= 20:
        display.set_pixel(0,3,9)
    if id >= 10:
        display.set_pixel(0,4,9)
    
    mod = id % 10
    if mod >= 1:
        display.set_pixel(4,4,9)
    if mod >= 2:
        display.set_pixel(4,3,9)
    if mod >= 3:
        display.set_pixel(4,2,9)
    if mod >= 4:
        display.set_pixel(4,1,9)
    if mod >= 5:
        display.set_pixel(4,0,9)
    if mod >= 6:
        display.set_pixel(3,4,9)        
    if mod >= 7:
        display.set_pixel(3,3,9)        
    if mod >= 8:
        display.set_pixel(3,2,9)
    if mod >= 9:
        display.set_pixel(3,1,9)
        
uart.init(9600, 8, None, 1, tx = pin1)
def fire():
    global id
    uart.write(bytes([id+1]))

updateScreen()
while True:
    if button_b.is_pressed():
        bReady = False
        nextID()
        updateScreen()
        while button_b.is_pressed(): pass
    if button_a.is_pressed():
        for x in range(5):
            for y in range(5):
                pv = display.get_pixel(x,y)
                if pv: display.set_pixel(x,y,4)
        fire()
        while button_a.is_pressed(): pass
        updateScreen()