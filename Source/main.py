import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
# overlay_img = cv2.imread('laughingMan.png', cv2.IMREAD_UNCHANGED)
# ratio = overlay_img.shape[1] / overlay_img.shape[0]

boundingBox = {
    "x":0,
    "y":0,
    "w":0,
    "h":0
}

while True:
    ret, img = cap.read()

    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) != 0: 
            for (x, y, w, h) in faces:
                boundingBox["x"] = x
                boundingBox["y"] = y
                boundingBox["w"] = w 
                boundingBox["h"] = h
                # Attempt at adding image
                # overlay_img = cv2.resize(overlay_img, (w,h)) 
                # bg = img[y:y+h, x:x+w]
                # np.multiply(bg, np.atleast_3d(255 - overlay_img[:, :, 3])/255.0, out=bg, casting="unsafe")
                # np.add(bg, overlay_img[:, :, 0:3] * np.atleast_3d(overlay_img[:, :, 3]), out=bg)
                # newImg = img[y:y+h, x:x+w] = bg

                img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), -1)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
        else:
            img = cv2.rectangle(img, (boundingBox['x'], boundingBox['y']), (boundingBox['x']+boundingBox['w'], boundingBox['y']+boundingBox['h']), (255, 0, 0), -10)
                    
        cv2.imshow('img', img)
    else:
        break 


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
