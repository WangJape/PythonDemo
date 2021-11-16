# pip install opencv_python
import cv2

# 0代表电脑摄像头，1代表外接摄像头(usb摄像头)
cap = cv2.VideoCapture(0)
cap.set(3, 900)  # 设置界面宽
cap.set(4, 900)  # 设置界面高

# 录制写入文件
codec = cv2.VideoWriter_fourcc(*'MJPG')
fps = 40.0
frameSize = (640, 480)
out = cv2.VideoWriter('video.avi', codec, fps, frameSize)
print("按键Q-结束视频录制")

# 视频显示
while cap.isOpened():
    # 第一个值为布尔值，如果视频正确，那么就返回true,  第二个值代表图像三维像素矩阵
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow("Capture", frame)
    inputKey = cv2.waitKey(25)  # 等待输入25ms
    if inputKey == ord('s'):  # ord()返回对应十进制整数
        print(cap.get(3))  # 界面宽
        print(cap.get(4))  # 界面高
    elif inputKey == ord('q'):
        print('完成')
        break
cap.release()
out.release()
cv2.destroyAllWindows()
