#This is the code for cropping the image to passport size using mouse events
#Here either use the image captured from im_capture.py or use any other image like tom.jpg
# India Passport Size: 35mm x 45mm = 413 x 531 pixels at 300 DPI
import cv2 
import numpy as np




frame = cv2.imread('tom.jpg')#here replace with tom.jpg if you want to use that image



   
draw = False
p1 = (0, 0)
p2 = p1
cropped = None  

def mouseClick(event, x, y, flags, param):
    global frame, draw, p1, p2, cropped
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        p1 = (x, y)
        p2 = p1
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            p2 = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        p2 = (x, y)
cv2.namedWindow("Original Image")
cv2.setMouseCallback("Original Image",mouseClick)

while True:
    temp = frame.copy()
    if draw == True:
        cv2.rectangle(temp, p1, p2, (0, 255, 0), 2)
    cv2.imshow("Original Image", temp)
    
   
    x1, y1 = p1
    x2, y2 = p2

    # Check for a valid rectangle 
    if abs(x2 - x1) > 5 and abs(y2 - y1) > 5:
        # Ensure coordinates are in correct order
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        
        
        cropped_region = frame[y1:y2, x1:x2]
        
        # Resize to passport size (413 x 531 pixels)
        cropped = cv2.resize(cropped_region, ( 413,531))
        
       
        display_img = cropped.copy()
       
        cv2.imshow("Passport Size Preview", display_img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if cropped is not None:
    cv2.imwrite("passport_photo.jpg", cropped)
    print("Passport-sized photo saved as 'passport_photo.jpg'")
  

cv2.waitKey(0)
cv2.destroyAllWindows()