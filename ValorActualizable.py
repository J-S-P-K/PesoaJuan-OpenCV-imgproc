import cv2

def actualizar_umbral(valor):
    _, binaria = cv2.threshold(gris, valor, 255, cv2.THRESH_BINARY)
    cv2.imshow("Blanco y negro", binaria)

# Cargar imagen
img = cv2.imread("img.jpeg")
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Crear ventana y trackbar
cv2.namedWindow("Blanco y negro")
cv2.createTrackbar("Umbral", "Blanco y negro", 128, 255, actualizar_umbral)

# Mostrar resultado inicial
actualizar_umbral(128)
cv2.waitKey(0)
cv2.destroyAllWindows()