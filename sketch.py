import cv2

img_location = 'E:/'
filename = 'Cat.png'
img = cv2.imread(img_location+filename)
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
inverted_gray = 255-gray_img
blurred_img = cv2.GaussianBlur(inverted_gray, (21,21),0)
inverted_blurred = 255-blurred_img
sketch_img = cv2.divide(gray_img, inverted_blurred, scale=256.0)
cv2.imshow('New Image', sketch_img)
cv2.waitKey(0)
