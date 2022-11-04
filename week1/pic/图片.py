# "C:\Users\1\Downloads\python-icon.png"
import cv2 as c
import numpy as np
import imutils as imu
color_python=c.imread("D:\codepra\code\.vscode\python\creator_space\week1\pic\python-icon.png",1)
gray_python=c.imread("D:\codepra\code\.vscode\python\creator_space\week1\pic\python-icon.png",0)
origin_python=c.imread("D:\codepra\code\.vscode\python\creator_space\week1\pic\python-icon.png",-1)
c.imshow('RGB',imu.resize(color_python,400))
c.imshow('gray',imu.resize(gray_python,400))
c.imshow('origin',imu.resize(origin_python,400))
c.imwrite('gray python.png',gray_python)
print('按"esc"键关闭所有窗口')
if c.waitKey(0) == 27:
    c.destroyAllWindows()
