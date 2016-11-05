import cv2
import numpy as np


def spawn(triangle):
    def mid_point(p1, p2):
        return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    a, b, c = triangle
    left = mid_point(a, b)
    right = mid_point(a, c)
    bottom = mid_point(b, c)
    yield [a, left, right]
    yield [left, b, bottom]
    yield [right, bottom, c]


def fractal(triangles, func):
    shapes2 = []
    map(lambda triangle: map(lambda t: shapes2.append(t), func(triangle)), triangles)
    return shapes2


def draw_triangles(triangles):
    im = np.zeros((1000, 1000))
    map(lambda triangle: cv2.fillConvexPoly(im, np.array(triangle), 255), triangles)
    cv2.imshow('Sierpinski', im)
    cv2.waitKey(100)


triangles = [[(500, 10), (10, 990), (990, 990)]]

for a in xrange(10):
    draw_triangles(triangles)
    triangles = fractal(triangles,spawn)

cv2.waitKey()
cv2.destroyAllWindows()
