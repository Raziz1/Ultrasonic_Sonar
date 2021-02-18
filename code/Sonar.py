#!/usr/bin/env python3

##### Servo SG90 #####
# 5v
# GND
# GPIO25 (Extension Board GPIO25)

##### UltraSonic Arduino #####
# VCC - 5v
# GND - GND
# TRIG - GPIO17
# ECHO - GPIO18


#Import Libraries
import RPi.GPIO as GPIO
import pygame
from pygame.locals import*
import math
import time

#Set up GPIO pins
TRIG = 11
ECHO = 12
servo = 22

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(servo,GPIO.OUT)
p=GPIO.PWM(servo,50)# 50hz frequency
p.start(0)# starting duty cycle ( it set the servo to 0 degree

#Initialize array of points
point=[0]*12
#Initalize scanner arm
angle=0
radius=0
    
#Set the angle of the servo motor    
def SetAngle(angle):
    #The duty cycle is dependent on the PWM (Pulse width modulation)
    #1ms pulse results in 0 degree movement
    #1.5ms pulse results in 90 degree movement
    #2ms pulse results in 180 degree movement
    duty = angle / 18 + 2
    GPIO.output(servo, True)
    p.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo, False)
    p.ChangeDutyCycle(0) 
    
def distance():
    #Clear the TRIG pin output
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)

    #Send an ultrasonic output
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)
    
    #Receive ultrasonic pulse and determine time taken to send and receive
    while GPIO.input(ECHO) == 0:
        a = 0
    time1 = time.time()
    while GPIO.input(ECHO) == 1:
        a = 1
    time2 = time.time()
    
    #Calculate the distance traveled given the speed of sound (340m/s) and divide by two given the pulse travles towards and obejct and returns
    during = time2 - time1
    return during * 340/2 *100

def loop():
        #Return the distance and add it to our array of points
        dis = distance()
        point.append(round(int(dis))) #Round and convert to int
        #print (dis, 'cm')
        #print ('')
        time.sleep(0.3)

    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sx = 500   # Desired physical surface size, in pixels.
    surface_sy = 500
    
    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sx, surface_sy))
        
    # Set up some data to describe a small rectangle and its color
    # A color is a mix of (Red, Green, Blue)
    some_color = (0, 255, 0)        
    point_color=(255,0,0)
    scanner_color=(0,255,0)
    while True:         #####Main Graphics LOOP #####
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 0,0 ))
        
        #Draw sonar arcs (No distance relation just random)
        pygame.draw.circle(main_surface, some_color, (int(surface_sx/2),int(surface_sy/2)),(int(surface_sx/2)),1)
        pygame.draw.circle(main_surface, some_color, (int(surface_sx/2),int(surface_sy/2)),(int(surface_sx/2.5)),1)
        pygame.draw.circle(main_surface, some_color, (int(surface_sx/2),int(surface_sy/2)),(int(surface_sx/4)),1)
        pygame.draw.circle(main_surface, some_color, (int(surface_sx/2),int(surface_sy/2)),(int(surface_sx/8)),1)
        
        #For each point (Every 15 degrees) calculate its x and y coordinates
        for i in range (len(point)):
            #Convert from radians to degrees 
            y=int(math.sin((i*15)*math.pi/180)*point[i])
            x=int(math.cos((i*15)*math.pi/180)*point[i])
            #print(x,",",y)
            #Draw the points
            pygame.draw.circle(main_surface,point_color,(int(surface_sx/2)+(x),int(surface_sy/2)+(y)),4,0)
        
        #Draw sonars spinning arm
        global angle
        global r
        angle+=2
        r=surface_sx/2
        a=math.sin(angle*math.pi/180)*r
        b=math.cos(angle*math.pi/180)*r
        pygame.draw.line(main_surface,scanner_color,(int(surface_sx/2),int(surface_sy/2)),(int(surface_sx/2)-int(a*2),int(surface_sy/2)-int(b*2)),2)
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

##### Main Python #####
if __name__ == "__main__":
    try:
        #Reset the servo
        SetAngle(0)
        # For the size of points rotate 15 degrees & calculate distance
        for l in range (len(point)):
            SetAngle(l*15)
            loop()
        #Stop the GPIO pins and cleanup 
        p.stop()
        GPIO.cleanup()
        #Draw sonar scope
        main()
    except KeyboardInterrupt:
        exit()

