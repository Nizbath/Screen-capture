from PIL import ImageGrab
import numpy as np
import cv2
while True:
    pic=ImageGrab.grab(bbox=(0,0,1280,720))
    pic_np= np.array(pic)
    last_pic= cv2.cvtColor(pic_np,cv2.COLOR_BGR2RGB)
    cv2.imshow('MOM',last_pic)
    cv2.waitKey(10)