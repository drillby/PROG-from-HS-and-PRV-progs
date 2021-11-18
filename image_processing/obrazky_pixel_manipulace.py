import cv2
import random

obrazek = cv2.imread("image_processing/fotky/pokus.jpg", -1)

for rada in range(100):
    # img.shape -> [rada, sloupec, kanal]
    for sloupec in range(obrazek.shape[1]):
        obrazek[rada][sloupec] = [random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255)]
#  prvních 100 řad bude mít random barvu pixelů

copy = obrazek[200: 300, 200: 300]
# vezme pole pixelů na x od 200 do 3OO, na y od 200 do 300

obrazek[500:600, 500:600] = copy
# dá pole pixelů na pozici co je v poli

cv2.imshow('pokus', obrazek)  # vykreslí obrázek

cv2.waitKey(0)  # čeká nekonečně dlouho na stisknutí klávesy
cv2.destroyAllWindows()
