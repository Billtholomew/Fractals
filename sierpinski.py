import cv2
import math
import numpy as np
import time

def spawn(triangle):
    def mid_point(p1,p2):
        return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
    a,b,c = triangle
    aLeft = mid_point(a,b)
    aRight = mid_point(a,c)
    aBottom = mid_point(b,c)
    tTop = [a,aLeft,aRight]
    tLeft = [aLeft,b,aBottom]
    tRight = [aRight,aBottom,c]
    return [tTop,tLeft,tRight]

def fractal(shapes,func):
    for _ in xrange(len(shapes)):
        shapes += func(shapes.pop(0))
    return shapes

def draw_triangles(triangles):
    im = np.zeros((1000,1000,3))
    for triangle in triangles:
        a,b,c = triangle
        a = tuple(map(int,a))
        b = tuple(map(int,b))
        c = tuple(map(int,c))
        cv2.line(im,a,b,(255,255,255))
        cv2.line(im,c,b,(255,255,255))
        cv2.line(im,a,c,(255,255,255))
    im = cv2.resize(im, (0,0), fx=0.5, fy=0.5) 
    cv2.imshow('Sierpinski',im)
    cv2.waitKey(100)


triangles = [[(500,10),(10,990),(990,990)]]

for a in xrange(10):
    draw_triangles(triangles)
    triangles = fractal(triangles,spawn)

cv2.waitKey()
cv2.destroyAllWindows()
