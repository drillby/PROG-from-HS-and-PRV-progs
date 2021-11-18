import cv2

obrazek = cv2.imread("image_processing/fotky/pokus.jpg", -1)

obrazek = cv2.resize(obrazek, (0, 0), fx=0.5, fy=0.5)

# jakým číslem se vynásobí počet pixelů

obrazek = cv2.resize(obrazek, (400, 600))  # počet pixelů

obrazek = cv2.rotate(obrazek, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

#  cs2.IMREAD_COLOR, nebo -1 = načte obrazek bez alfy
#  cs2.IMREAD_GRAYSCALE, nebo 0 = načte obrázek černobíle
#  cs2.IMREAD_UNCHANGED, nebo 1 = načte obrázek s alfou

# vytvoří jpg z mnou upravenýho obrázku
cv2.imwrite("pokus_vytvoreni.jpg", obrazek)

cv2.imshow('pokus', obrazek)  # vykreslí obrázek

cv2.waitKey(0)  # čeká nekonečně dlouho na stisknutí klávesy
cv2.destroyAllWindows()
