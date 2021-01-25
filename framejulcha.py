import numpy as np
import tkinter
from PIL import Image
from PIL import ImageTk
import cv2

window = tkinter.Tk()
window.title("face")
window.geometry()
window.resizable(1, 1)

def right_rotation():#오른쪽으로 회전하는 함수
    global src
    height, width, channel = src.shape
    matrix = cv2.getRotationMatrix2D((width*0.5, height*0.5), -5, 1)# 사진 중심을 기준으로 5도 회전
    right_rotate_image = cv2.warpAffine(src, matrix, (width, height))#오린쪽 으로 회전한 이미지 연산
    src = right_rotate_image
    show(right_rotate_image)


def left_rotation():
    global src
    height, width, channel = src.shape
    matrix = cv2.getRotationMatrix2D((width*0.5, height*0.5), 5, 1)
    left_rotate_image = cv2.warpAffine(src, matrix, (width, height))
    src = left_rotate_image
    show(left_rotate_image)

def scale_up():
    global src
    height, width, channel = src.shape
    dst = cv2.pyrUp(src, dstsize = (width*2, height*2), \
    borderType = cv2.BORDER_DEFAULT);#줄넘김
    src = dst
    show(dst)

def scale_down():
    global src
    height, width, channel = src.shape
    dst2 = cv2.pyrDown(src, dstsize = (int(width*0.5), int(height*0.5)),\
    borderType = cv2.BORDER_DEFAULT);#줄넘김
    src = dst2    
    show(dst2)

def tilt():
    global src
    height, width, channel = src.shape
    srcPoint = np.array([[300, 100], [400, 100], [800, 800], [200, 800]],\
    dtype = np.float32)#줄넘김
    dstPoint = np.array([[0, 0], [width, 0], [width, height], [0, height]],\
    dtype = np.float32)#줄넘김
    matrix = cv2.getPerspectiveTransform(srcPoint, dstPoint)
    dst = cv2.warpPerspective(src, matrix, (width, height))
    src = dst
    show(dst)


def close():
    window.quit()
    window.destroy()


def hue():
    h, s, v = cv2.split(hsv)
    cv2.imshow("hue", h)

def saturation():
    h, s, v = cv2.split(hsv)
    cv2.imshow("saturation", s)

def value():
    h, s, v = cv2.split(hsv)
    cv2.imshow("value", v)

def show(image):
    cv2.imshow("show", image)
    src=image

src = cv2.imread("gallery\park.jpg", cv2.IMREAD_COLOR)
img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
img = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image = img)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)



label = tkinter.Label(window, image = imgtk)
label.pack(side = "top")

menubar = tkinter.Menu(window)

menu_1 = tkinter.Menu(menubar, tearoff = 0)
menu_1.add_command(label = "right_rotation", command = right_rotation)
menu_1.add_command(label = "left_rotation", command = left_rotation)
menubar.add_cascade(label = "회전", menu = menu_1)

menu_2 = tkinter.Menu(menubar, tearoff = 0)
menu_2.add_command(label = "확대",command = scale_up)
menu_2.add_command(label = "축소", command = scale_down)
menubar.add_cascade(label = "확대/축소", menu=menu_2)

menu_3 = tkinter.Menu(menubar, tearoff = 0)
menu_3.add_command(label = "tilt", command = tilt)
menu_3.add_command(label = "close", command = close)
menubar.add_cascade(label = "tilt/종료", menu = menu_3)

menu_4 = tkinter.Menu(menubar, tearoff = 0)
menu_4.add_command(label = "h", command = hue)
menu_4.add_command(label = "s", command = saturation)
menu_4.add_command(label = "v", command = value)
menubar.add_cascade(label = "hsv", menu = menu_4)

window.config(menu = menubar)

window.mainloop()