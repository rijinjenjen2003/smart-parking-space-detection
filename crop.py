import cv2
image = cv2.imread(r"C:\Users\rijin\Downloads\DSu68.jpg")
x = 100
y = 100
w = 150
h = 180
cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.rectangle(image, (180,100), (280,280), (0,255,0), 2)
slot=image[y:y+h,x:x+w]
cv2.imshow("Original", image)
cv2.imshow("Parking Slot", slot)

cv2.waitKey(0)
cv2.destroyAllWindows()