import cv2

face_cascade = cv2.CascadeClassifier("data/Files/haarcascade_frontalface_default.xml")

img = cv2.imread("data/Files/news.jpg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey_img, scaleFactor=1.05, minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow("Grey", img)
cv2.waitKey()
cv2.destroyAllWindows()
