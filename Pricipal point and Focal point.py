import cv2 as cv
import numpy as np
import math
import glob
from matplotlib import pyplot as plt
import os

image = cv.imread("vanishing_point_images/3_vanishingpoint_.jpg",cv.IMREAD_UNCHANGED)

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

line = cv.line(image, (27,391), (1006,508), (255,0,0),8) # Blue Line 1
line = cv.line(image, (1137,408), (16,411), (255,0,0),8) # Blue Line 2 
line = cv.line(image, (720,8), (613,790), (0,255,0),8) # Green Line 1
line = cv.line(image, (732,19), (411,705), (0,255,0),8) # Green Line 2
line = cv.line(image, (510,298), (645,762), (0,0,255),8) # Red Line 1
line = cv.line(image, (566,259), (637,788), (0,0,255),8) # Red Line 2

cv.imwrite('Vanishing_Lines.jpg', line)

def Vanishing_point(x1, y1, x2, y2, x3, y3, x4, y4):
   a1= y2-y1
   a2= y4-y3
   b1= x1-x2
   b2= x3-x4
   c1=(y1*(x2-x1))- (x1* (y2-y1))
   c2=(y3*(x4-x3))- (x3* (y4-y3))

   x= ((b1*c2) - (b2*c1))/((a1*b2)- (a2*b1))
   y= ((c1*a2) - (c2*a1))/((a1*b2)- (a2*b1))

   return x, y

VP1_x, VP1_y = Vanishing_point(27,391,1006,508,1137,408,16,411)
VP2_x, VP2_y = Vanishing_point(720,8,613,790,732,19,411,705)
VP3_x, VP3_y = Vanishing_point(510,298,645,762,566,259,637,188)


print('\nVanishing Point 1 x and y coordinates', VP1_x, VP1_y)
print('\nVanishing Point 1 x and y coordinates', VP2_x, VP2_y)
print('\nVanishing Point 1 x and y coordinates', VP3_x, VP3_y)

u1 = VP1_x
v1 = VP1_y
u2 = VP2_x
v2 = VP2_y
u3 = VP3_x
v3 = VP3_y

A_matrix = np.matrix([[ u1 - u3, v1 - v3], [ u2 - u3, v2 - v3]])
B_matrix = np.matrix([[ (u1 - u3) * u2 + (v1 - v3) * v2], [ (u2 - u3) * u1 + (v2 - v3) * v1]])


X_matrix = np.linalg.inv(A_matrix) * B_matrix
x0 = float(X_matrix[0]) # Extracting data from X as x0
y0 = float(X_matrix[1]) # Extracting data from X as y0

print('\nPrincipal Points  : \nX0 = ', x0, '\nY0 = ', y0)


# Finding the focal length



f = math.sqrt(math.fabs((-(u1 - x0) * (u2 - x0)) - ((v1 - y0) * (v2 - y0)))) # Focal Point

print('\nThe focal point of the ipad air camera is : ', f)
