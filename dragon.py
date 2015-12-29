import cv2
import math
import numpy as np
import time

def fold_line(line,flipFlop):
    start = line[0:2]
    end = line[2:4]
    dX = end[0]-start[0]
    dY = end[1]-start[1]
    length = math.sqrt(dX**2+dY**2)
    angle = math.atan2(dY,dX)
    leg = np.cos(math.pi/4)*length
    if flipFlop:
        angle += math.pi/4
    else:
        angle -= math.pi/4
    newEnd = [p for p in start]
    newEnd[0] += math.cos(angle)*leg
    newEnd[1] += math.sin(angle)*leg
    line1 = [start[0],start[1],newEnd[0],newEnd[1]]
    line2 = [newEnd[0],newEnd[1],end[0],end[1]]
    return line1,line2

def fold_lines(lines):
    flipFlop = True
    for lindex in xrange(len(lines)):
        line = lines.pop(0)
        line1,line2 = fold_line(line,flipFlop)
        lines.append(line1)
        lines.append(line2)
        flipFlop = not flipFlop

def draw_lines(lines):
    im = np.zeros((1000,1000,3))
    for line in lines:
        line = [int(i) for i in line]
        P1 = (line[0],line[1])
        P2 = (line[2],line[3])
        cv2.line(im,P1,P2,(255,255,255))
    im = cv2.resize(im, (0,0), fx=0.5, fy=0.5) 
    cv2.imshow('Dragon',im)
    cv2.waitKey(100)
    
line = [250,500,750,500]
lines = [line]
for a in xrange(16):
    draw_lines(lines)
    fold_lines(lines)

print 'Complete'
