import numpy as np
import cv2

kamera = cv2.VideoCapture(0)  # číslování jako v poli, je možný tam dát i video

bezi = True
while bezi:
    ret, sminek = kamera.read()
    sirka = int(kamera.get(3))
    vyska = int(kamera.get(4))

    # konvertuje bgr na hsv (hue saturation and lightness)
    hsv = cv2.cvtColor(sminek, cv2.COLOR_BGR2HSV)
    lower_modra = np.array([90, 50, 50])  # hsv hodnoty
    upper_modra = np.array([130, 255, 255])

    maska = cv2.inRange(hsv, lower_modra, upper_modra) # vrátí 1 a 0 podle toho jestli je detekovaná barva v rozsahu lower_blue a upper_blue

    vysledek = cv2.bitwise_and(sminek, sminek, mask=maska)

    cv2.imshow("okno", vysledek)

    if cv2.waitKey(1) == ord("q"):
        bezi = False

kamera.release()
cv2.destroyAllWindows()
