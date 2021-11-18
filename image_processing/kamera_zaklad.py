import numpy as np
import cv2

kamera = cv2.VideoCapture(0)  # číslování jako v poli, je možný tam dát i video

bezi = True
while bezi:
    ret, sminek = kamera.read()
    sirka = int(kamera.get(3))
    vyska = int(kamera.get(4))

    snimek = cv2.line(sminek, (0, 0), (sirka, vyska), (255, 0, 0), 10)
    # ! opencv bere bgr, ne rgb
    snimek = cv2.line(sminek, (0, vyska), (sirka, 0), (0, 255, 0), 5)

    snimek = cv2.rectangle(snimek, (100, 100), (200, 200), (128, 128, 128), 5)
    # horni levy roh a dolni pravy roh, -1 pro fill

    snimek = cv2.circle(snimek, (400, 400), 20, (0, 0, 255), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    snimek = cv2.putText(snimek, "A-hoj", (200, vyska - 20),
                         font, 2, (0, 0, 0), 5, cv2.LINE_AA)  # lokace dolni leva, za fontem velikost pisma, predposledni je tloustka

    cv2.imshow("okno", sminek)

    if cv2.waitKey(1) == ord("q"):
        bezi = False

kamera.release()
cv2.destroyAllWindows()
