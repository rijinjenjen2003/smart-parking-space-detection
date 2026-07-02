import cv2
import pickle

image = cv2.imread(r"C:\Users\rijin\Downloads\ChatGPT Image Jul 2, 2026, 01_45_45 PM.jpg")
positions=[]
width=100
height=180

def mouseClick(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        positions.append((x,y))
        print(positions)
        with open("position.pkl","wb") as file:
            pickle.dump(positions,file)
    if event==cv2.EVENT_RBUTTONDOWN:
        print("Right click")
        print('X=',x)
        print('Y=',y)
        for i,pos in enumerate(positions):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                positions.pop(i)
                break
while True:

    img_copy = image.copy()

    for pos in positions:

        cv2.rectangle(
            img_copy,
            pos,
            (pos[0]+width, pos[1]+height),
            (0,255,0),
            2
        )

    cv2.imshow("Parking", img_copy)
    cv2.setMouseCallback(
        "Parking",
        mouseClick
    )

    cv2.waitKey(1)
