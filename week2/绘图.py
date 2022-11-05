#opencv绘制直线使用`cv2.line()`函数
import cv2 as c
import numpy as np
#首先创建一个新的纯白色图片，作为画板
img=np.ones((200,200,3))
img*=255#将颜色调成白色
#用cv2.line()绘制直线
#参数分别为绘制对象、起始坐标、结束坐标、颜色、线条粗细
c.line(img,(100,200),(0,0),(0,255,0),1)
c.line(img,(100,200),(200,0),(0,0,255),3)
c.line(img,(200,0),(0,100),(0,0,255),3)
c.line(img,(0,100),(200,100),(0,0,255),3)
c.line(img,(200,100),(0,0),(0,0,255),3)
#用cv2.circle()绘制圆，用cv2.polylines()绘制三（多）边形
img1=np.ones((200,200,3),np.uint8)#再来一个画板
img1*=255#将颜色调成白色
c.circle(img1,(100,100),100,(0,0,255),1)
c.circle(img1,(130,60),15,(0,0,255),1)
c.circle(img1,(70,60),15,(0,0,255),1)
pts=np.array([[75,130],[125,130],[100,155]])#设置三顶点坐标

c.polylines(img1,[pts],True,(0,0,255),2)
c.imshow("star",img)
c.imshow("smile",img1)
c.imwrite('star.jpg',img)
c.imwrite('smile.jpg',img1)
if c.waitKey(0)== 27:
    c.destroyAllWindows()