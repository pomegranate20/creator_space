# 创客空间第一周任务
## 一、opencv 的安装配置
1. 在控制台中执行` pip install opencv-python`命令，安装opencv库
2. 在python文件中使用 `import cv2` 以导入opencv库
## 二、对于图片的处理
1. `cv2.imread('picture_path',x)`读取图片

    其中，'picture_path'是你要读取的图片文件地址；

    x的含义为：对于图片，无视透明度显示为1，黑白为0，不变为-1。
2. `cv2.imshow()`展示图片 \
   另外可以通过导入imutils库，`imutils.resize(cap,size)`来实现展示图片的大小调整。
3. `cv2.imwrite('pic_name',target)`保存图片
## 三、对于视频的处理
1. `cv2.VideoCapture()`读取视频，可选择网络摄像头（此时括号里为摄像头编号），也可以选择视频文件（此时应为文件路径）
2. `cv2.imshow()`展示视频
3. `cv2.VideoWriter`保存视频，需要注意的是应当给出四个参数，分别是文件名、编码类型、帧率、宽高