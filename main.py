###############################
# Read the README file first  #
###############################

import cv2 as cv
import numpy as np
import os


test_img_path = 'mask_27.jpg'


test_img = cv.imread(test_img_path, cv.IMREAD_UNCHANGED)
cascade = cv.CascadeClassifier('cascade/cascade.xml')
rectangles = cascade.detectMultiScale(test_img)


if len(rectangles):

    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    for (x, y, w, h) in rectangles:

        top_left = (x, y)
        bottom_right = (x + w, y + h)
        cv.rectangle(test_img, top_left, bottom_right, color=line_color, lineType=line_type, thickness=2)

    cv.imshow('result', test_img)
    cv.waitKey(0)
else:
    print("can't find any mask ")

cv.destroyAllWindows