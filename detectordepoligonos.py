import cv2
import numpy

image = cv2.imread('cuadrado_blanco.jpg')
#cv2.imshow('image',image)
print(image.shape)

reducida = cv2.resize(image, (640, 480))
#cv2.imshow('reducida', reducida)
#cv2.waitKey(0)
print(reducida.shape)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #pasa la imagen a grises
#cv2.imshow('gris', gray)

print(gray.shape)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#cv2.imshow('hsv', hsv)
#cv2.waitKey(0)
print(hsv.shape)

canny = cv2.Canny(gray, 10, 150) #convierte la imagen en linias blanacas finas en un fondo negro

#Centroide 

dilate = cv2.dilate(canny, None, iterations=10) #vuelve las linias blancas más anchas, las dilata


#Sacar el centroide mediante las coordenadas de los vertices en la variable cnts


erode = cv2.erode(dilate, None, iterations=10) #hace los huecos negros que dejan las linias blancas más grandes



#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
#_,cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 3
invertir = cv2.bitwise_not(erode)


cnts, _ = cv2.findContours(invertir, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 4

for i in cnts:
    M = cv2.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.drawContours(image, [i], -1, (0, 255, 0), 2)
        cv2.circle(image, (cx, cy), 2, (0, 0, 255), -1)
    print(f"x: {cx} y: {cy}")

x=[cx,cy]
print(x)


cv2.drawContours(image, cnts, -1, (0,255,0), 2)
cv2.imshow('imagen',image)
cv2.waitKey(0)