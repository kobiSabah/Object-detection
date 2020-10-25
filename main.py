##########################################
# You should read the README file first ##
##########################################

import cv2 as cv
import numpy as np
import os


test_img_path = 'mask_27.jpg'


test_img = cv.imread(test_img_path, cv.IMREAD_UNCHANGED)
cascade_limetone = cv.CascadeClassifier('cascade/cascade.xml')
rectangles = cascade_limetone.detectMultiScale(test_img)


if len(rectangles):

    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    # Loop over all the rectangles
    for (x, y, w, h) in rectangles:

        # Determine the box position
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        # Draw the box
        cv.rectangle(test_img, top_left, bottom_right, color=line_color, 
                        lineType=line_type, thickness=2)

    cv.imshow('result', test_img)
    cv.waitKey(0)
else:
    print("can't find any mask ")

cv.destroyAllWindows