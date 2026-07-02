import cv2
import pickle
import numpy as np

with open("position.pkl", "rb") as file:
    positions = pickle.load(file)

print(positions)
free=0

image = cv2.imread(r"C:\Users\rijin\Downloads\ChatGPT Image Jul 2, 2026, 01_45_45 PM.jpg")
for pos in positions:
    x,y=pos
    slot=image[y:y+180,x:x+100]
    cv2.imshow("Slot", slot)
    cv2.waitKey(0)
    gray=cv2.cvtColor(slot,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(3,3),1)
    _,threshold=cv2.threshold(blur,80,255,cv2.THRESH_BINARY)
    kernal=np.ones((3,3),np.uint8)
    dilate=cv2.dilate(threshold,kernal,iterations=2)
    white=cv2.countNonZero(dilate)
    print("White Pixels:", white)
    cv2.putText(
    image,
    str(white),
    (x, y-5),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.4,
    (255,255,255),
    1
)
    if white>100:
        color=(0,0,255)
    else:
        color=(0,255,0)
        free+=1
    cv2.rectangle(
    image,
    (x,y),
    (x+100,y+180),
    color,
    2
)
cv2.imshow("Parking Detector", image)

cv2.waitKey(0)

cv2.destroyAllWindows()
