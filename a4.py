import cv2
import os

dataset = "dataset"
name = "akash"

path = os.path.join(dataset, name)
if not os.path.isdir(path):
    os.mkdir(path)

(width, height) = (130, 130)

alg = "haarcascade_frontalface_alt2.xml"

haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(2)

count = 1
while count < 31:

    print("No Person Detected")
    _, img = cam.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        faceOnly = grayImg[y:y + h, x:x + w]
        resizeImg = cv2.resize(faceOnly, (width, height))
        cv2.imwrite("%s/%s.jpg" % (path, count), resizeImg)
        print("Person Detected")
        count += 1
    cv2.imshow("FaceDetection", img)
    key = cv2.waitKey(10)
    if key == 27:
        break
print("Image Captured Successfully")
cam.release()
cv2.destroyAllWindows()