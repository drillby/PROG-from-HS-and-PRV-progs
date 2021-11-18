import numpy as np
import cv2
import random

obrazek = cv2.imread("image_processing/fotky/chess.png")

seda = cv2.cvtColor(obrazek, cv2.COLOR_BGR2GRAY)
# převede bgr na šedou, algoritmy s tim pracují líp

rohy = cv2.goodFeaturesToTrack(seda, 100, 0.01, 10)
# obrazek, kolik rohů, minimální jistota, že je roh, minimální eukledovská vzdálenost(absolutní hodnota)
rohy = np.int0(rohy)

for roh in rohy:
    x, y = roh.ravel()
    cv2.circle(obrazek, (x, y), 5, (255, 0, 0), -1)

for i in range(len(rohy)):
    for j in range(i + 1, len(rohy)):
        roh1 = tuple(rohy[i][0])
        roh2 = tuple(rohy[j][0])
        barva1 = random.randint(0, 255)
        barva2 = random.randint(0, 255)
        barva3 = random.randint(0, 255)
        cv2.line(obrazek, roh1, roh2, (barva1, barva2, barva3), 1)
# spojí všechny rohy se všemi a čarám dá random barvu
cv2.imshow("Frame", obrazek)
cv2.waitKey(0)
cv2.destroyAllWindows()
