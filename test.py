import RPi.GPIO as g
import random as rand
import time

g.setmode(g.BCM)
btn1 = 14
btn2 = 15

led1 = 18
led2 = 23
led3 = 24
led4 = 25

c1 = False
s1 = False
c2 = False
s1 = False

g.setup(btn1, g.IN)
g.setup(btn2, g.IN)
g.setup(led1, g.OUT)
g.setup(led2, g.OUT)
g.setup(led3, g.OUT)
g.setup(led4, g.OUT)

def ledChange(a, b):
    if a == 1:
        global led1
        g.output(led1, b)
    elif a == 2:
        global led2
        g.output(led2, b)
    elif a == 3:
        global led3
        g.output(led3, b)
    else:
        global led4
        g.output(led4, b)

def pre1(c):
    global s1
    global c1
    s1 = not s1
    c1 = False

def pre2(c):
    global s2
    global c2
    s2 = not s2
    c2 = False

def run(click1, click2):
    if click1 and click2:
        a = rand.randrange(1, 5)
        b = rand.randrange(0, 2)
        ledChange(a, b)
    elif click1:
        ledChange(1, 0)
        ledChange(2, 0)
        ledChange(3, 1)
        ledChange(4, 1)
    elif click2:
        ledChange(1, 1)
        ledChange(2, 1)
        ledChange(3, 0)
        ledChange(4, 0)
    else:
        ledChange(1, 0)
        ledChange(2, 0)
        ledChange(3, 0)
        ledChange(4, 0)

g.add_event_detect(btn1, g.RISING)
g.add_event_detect(btn2, g.RISING)
g.add_event_callback(btn1, pre1)
g.add_event_callback(btn2, pre2)

try:
    while True:
        time.sleep(0.01)
        click1 = g.input(btn1)
        click2 = g.input(btn2)
        if c1 or c2:
            if click1 and click2:
                a = rand.randrange(1, 5)
                b = rand.randrange(0, 2)
                ledChange(a, b)
            elif click1:
                ledChange(1, 0)
                ledChange(2, 0)
                ledChange(3, 1)
                ledChange(4, 1)
            elif click2:
                ledChange(1, 1)
                ledChange(2, 1)
                ledChange(3, 0)
                ledChange(4, 0)
            else:
                ledChange(1, 0)
                ledChange(2, 0)
                ledChange(3, 0)
                ledChange(4, 0)
           
except KeyboardInterrupt:
    pass

g.cleanup()
