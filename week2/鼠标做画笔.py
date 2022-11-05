import cv2 as c
import numpy as np
import math as m
#设置全局标志，来作为判断形状的依据
sign=0
start=(0,0)
#定义一个函数，说明不同标志的值会绘制什么图形
def draw(event,x,y,flag,param):
    global sign,start
    if event==c.EVENT_LBUTTONDOWN:#如果按下左键，记录此时鼠标位置，并作为起始坐标
        start=(x,y)
    elif event==c.EVENT_LBUTTONUP:
        if sign==0:#画直线
            c.line(img,start,(x,y),(0,0,255),1)
        if sign==1:#画矩形
            c.rectangle(img,start,(x,y),(0,0,255),1)
        if sign==2:#画圆，算出半径
            a=x-start[0]
            b=y-start[1]
            r=int(m.sqrt((a**2+b**2)))
            c.circle(img,(x,y),r,(0,0,225),1)
        if sign==3:#画文本
            text=input()
            c.putText(img,text,(x,y),c.FONT_HERSHEY_TRIPLEX,3,(200,15,15),3)
    


img=np.ones((500,500,3))
img *= 255
c.namedWindow('draw')
c.setMouseCallback("draw",draw)

while (True):
    c.imshow('draw',img)
    key=c.waitKey(1)
    if key==ord("q"):
        break
    if key==ord("l"):
        sign=0
    if key==ord("r"):
        sign=1
    if key==ord("c"):
        sign=2
    if key==ord("t"):
        sign=3
c.imwrite("draw.jpg",img)
c.destroyAllWindows()