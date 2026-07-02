import cv2
import numpy as np

image = cv2.imread(r"C:\Users\rijin\Downloads\DSu68.jpg")
positions = [

    (50,100),

    (170,100),

    (290,100),

    (410,100),

    (530,100),

    (650,100)

]
free = 0

for pos in positions:

    x, y = pos

    slot = image[y:y+180, x:x+100]

    gray = cv2.cvtColor(slot, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3,3), 1)

    _, thresh = cv2.threshold(
        blur,
        150,
        255,
        cv2.THRESH_BINARY
    )

    kernel = np.ones((3,3), np.uint8)

    dilate = cv2.dilate(
        thresh,
        kernel,
        iterations=1
    )

    white = cv2.countNonZero(dilate)

    if white > 1000:

        color = (0,0,255)

    else:

        color = (0,255,0)

        free += 1

    cv2.rectangle(
        image,
        (x,y),
        (x+100,y+180),
        color,
        2
    )

cv2.imshow("image",slot)
cv2.waitKey(0)
cv2.destroyAllWindows()