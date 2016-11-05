import cv2
import numpy as np


def fold_line(i, line):
    x1, y1, x2, y2 = line
    dx, dy = (x2 - x1, y2 - y1)
    angle = np.arctan2(dy, dx) + (-1) ** i * np.pi / 4
    leg = np.cos(np.pi / 4) * np.sqrt(dx ** 2 + dy ** 2)
    x3 = x1 + np.cos(angle) * leg
    y3 = y1 + np.sin(angle) * leg
    line1 = [x1, y1, x3, y3]
    line2 = [x3, y3, x2, y2]
    return map(int, line1), map(int, line2)


def fold_lines(lines):
    for i, line in enumerate(lines):
        line1, line2 = fold_line(i, line)
        yield line1
        yield line2


def draw_lines(lines):
    im = np.zeros((1000, 1000))
    map(lambda line: cv2.line(im, (line[0], line[1]), (line[2], line[3]), 255), lines)
    cv2.imshow('Dragon', im)
    cv2.waitKey(100)

lines = [[250, 500, 750, 500]]
for a in xrange(16):
    draw_lines(lines)
    lines = [line for line in fold_lines(lines)]

print 'Complete'
