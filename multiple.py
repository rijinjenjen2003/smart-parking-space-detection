import cv2

image = cv2.imread(r"C:\Users\rijin\Downloads\DSu68.jpg")


positions = [

    (50,100),

    (170,100),

    (290,100),

    (410,100),

    (530,100),

    (650,100)

]

for pos in positions:

    x,y = pos

    cv2.rectangle(

        image,

        (x,y),

        (x+100,y+180),

        (0,0,255),

        5

    )

cv2.imshow("Parking", image)

cv2.waitKey(0)

cv2.destroyAllWindows()