import cv2
cap = cv2.VideoCapture('D:\\codepra\\code\\.vscode\\python\\creator_space\week1\\video\\.mp4')
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output.mp4',fourcc,20.0,(width,height))
while True:
    ret, frame = cap.read()
    
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
