import cv2
import numpy as np



def filtcanny(img):

	image = cv2.imread(img)
	#cv2.imshow('image',image)
	#print(image)

	#reducida = cv2.resize(image, (640, 480))
	#cv2.imshow('reducida', reducida)
	#cv2.waitKey(0)
	#print(reducida)

	invertir = cv2.bitwise_not(image)
	#cv2.imshow('invertir', invertir)
	#cv2.waitKey(0)

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #pasa la imagen a grises
	#cv2.imshow('gris', gray)
	#cv2.waitKey(0)
	#print(gray)

	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	#cv2.imshow('hsv', hsv)
	#cv2.waitKey(0)
	#print(hsv)

	canny = cv2.Canny(gray, 10, 100) #convierte la imagen en linias blanacas finas en un fondo negro
	#cv2.imshow('canny', canny)
	#cv2.waitKey(0)
	

	dilate = cv2.dilate(canny, None, iterations=10) #vuelve las linias blancas más anchas, las dilata
	#cv2.imshow('dilate', dilate)
	#cv2.waitKey(0)

	#Sacar el centroide mediante las coordenadas de los vertices en la variable cnts


	erode = cv2.erode(dilate, None, iterations=10) #hace los huecos negros que dejan las linias blancas más grandes
	#cv2.imshow('erode', erode)
	#cv2.waitKey(0)


	#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
	#_,cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 3
	invertir = cv2.bitwise_not(erode)
	#cv2.imshow('invertir', invertir)
	#cv2.waitKey(0)


	cnts, jerarquia = cv2.findContours(invertir, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 4

	#print(jerarquia)

	for i in cnts:
		M = cv2.moments(i)
		if M['m00'] != 0:
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			cv2.drawContours(image, [i], -1, (0, 255, 0), 2)
			cv2.circle(image, (cx, cy), 2, (0, 0, 255), -1)
		#print(f"x: {cx} y: {cy}")

	#x=[cx,cy]
	#print(x)


	cv2.drawContours(image, cnts, -1, (0,255,0), 2)
	cv2.imshow('FILTRO CANNY',image)
	cv2.waitKey(0)
	
def filtmask(img):

	image = cv2.imread(img)
		# Convert BGR to HSV
	frame_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		#cv2.imshow('hsv', hsv)
		#cv2.waitKey(0)
		#print(hsv)

		# Threshold of white in HSV space
	pure_white_hsv = np.array([0, 0, 210])
	pale_gray_hsv = np.array([255, 15, 255])

		# Create and use the mask
	mask = cv2.inRange(frame_hsv, pure_white_hsv, pale_gray_hsv)
	frame_masked_hsv = cv2.bitwise_and(frame_hsv, frame_hsv, mask=mask)
		# Return to BGR format
	frame_result = cv2.cvtColor(frame_masked_hsv, cv2.COLOR_HSV2BGR)

	frame_gray = cv2.cvtColor(frame_result, cv2.COLOR_BGR2GRAY)
	cnts, _ = cv2.findContours(frame_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for i in cnts:
		M = cv2.moments(i)
		if M['m00'] != 0:
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			cv2.drawContours(image, [i], -1, (0, 255, 0), 2)
			cv2.circle(image, (cx, cy), 2, (0, 0, 255), -1)
		#print(f"x: {cx} y: {cy}")

	cv2.drawContours(image, cnts, -1, (0,255,0), 2)
	cv2.imshow('FILTRO MASCARA',image)
	cv2.waitKey(0)