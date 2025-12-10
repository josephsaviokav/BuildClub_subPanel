#Use this code to capture an image from webcam on mouse click and save it as 'clicked_image.jpg'

import cv2

#This function can be used to capture the image when the mouse is clicked 
def mouse_event(event,x,y,flags,param):
    if(event==cv2.EVENT_LBUTTONDOWN):
        print("saving image")
        cv2.imwrite("clicked_image.jpg",frame)
cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam",mouse_event)

#capturing the video
cam=cv2.VideoCapture(0)
while True:
    _,frame=cam.read()
    cv2.imshow("Webcam",frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
cv2.destroyAllWindows() 