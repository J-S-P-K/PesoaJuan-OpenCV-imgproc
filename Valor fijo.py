import cv2

# Cargar imagen
img = cv2.imread("img.jpg")

# Convertir a escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar umbral binario
umbral = 128  # Cambia este valor si querés
_, binaria = cv2.threshold(gris, umbral, 255, cv2.THRESH_BINARY)

# Mostrar resultado
cv2.imwrite("imagen_final.jpg", binaria)
