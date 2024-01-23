import numpy as np
import cv2

# Initialisations
startPoint = (0,0)
endPoint = (0,0)
drawing = False
erase = False
drawing_color = (0,0,0)  # Couleur de dessin initiale (noir)
thickness = 5

def nothing(x):
    pass

cv2.namedWindow('image')
# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# Fonction pour dessiner
def draw(event, x, y, flags, param):
    global startPoint, endPoint, drawing_color, drawing, thickness, erase
    if event == cv2.EVENT_LBUTTONDOWN:
        startPoint = (x, y)
        drawing = True
        erase = False
    elif event == cv2.EVENT_RBUTTONDOWN:
        startPoint = (x, y)
        erase = True
        drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            endPoint = (x, y)
            cv2.line(img, pt1=startPoint, pt2=endPoint, color=drawing_color, thickness=thickness)
            startPoint = endPoint
        if erase:
            endPoint = (x, y)
            cv2.line(img, pt1=startPoint, pt2=endPoint, color=(255,255,255), thickness=thickness)
            startPoint = endPoint

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    elif event == cv2.EVENT_RBUTTONUP:
        erase = False

    elif event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:  # Molette vers le haut
            thickness += 1
        else:  # Molette vers le bas
            thickness -= 1
        thickness = max(1, thickness)  # Épaisseur minimum de

# Créer une image blanche et une fenêtre
img = np.ones((600, 600, 3), np.uint8) * 255
cv2.setMouseCallback('image', draw)

while True:
    cv2.imshow('image', img)
    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    drawing_color = (b,g,r)
    key = cv2.waitKey(20) & 0xFF
    if key == ord('s'):
        cv2.imwrite('Saved_image.png', img)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
