#importar librerias
import cv2
import numpy as np

#determinar que colores detectar
redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)
redBajo2=np.array([175, 100, 20], np.uint8)
redAlto2=np.array([179, 255, 255], np.uint8)

#funciones para procesar la imagen (lineas 13 a 24)

#leer la imagen
img = cv2.imread('fondo.png')
#transformar bgr a hsv
hsv_form = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#detectar en la imagen los rangos determinados antes
maskRed1 = cv2.inRange(hsv_form, redBajo1, redAlto1)
maskRed2 = cv2.inRange(hsv_form, redBajo2, redAlto2)
maskRed = cv2.add(maskRed1, maskRed2)
#detectar la imagen pero con color, no binario como el anterior
maskRedvis = cv2.bitwise_and(img, img, mask = maskRed)
#visualizar la deteccion del objeto maskRed
cv2.imshow('mascara binario', maskRed)
#visualizar la deteccion del objeto pero con el color detectado
cv2.imshow('mascara color', maskRedvis)
#mostrar la imagen
cv2.imshow('Fondo prueba', img)

#funciones para que se cierre la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()