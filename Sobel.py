import numpy as np 
import cv2

img = cv2.imread('coffee-resized.jpg',0)
m,n = img.shape
img_new = np.zeros([m,n])
mask_h= np.array([[1,2,1],[0,0,0],[-1,-2,-1]],np.float32)
mask_v= np.array([[1,0,-1],[2,0,-2],[1,0,-1]],np.float32)
for i in range(1,m-1):
	for j in range(1,n-1):
		sobel_x= img[i-1,j-1]*mask_v[0,0]+img[i-1,j]*mask_v[0,1]+img[i-1,j+1]*mask_v[0,2]\
		+img[i,j-1]*mask_v[1,0]+img[i,j]*mask_v[1,1]+img[i,j+1]*mask_v[1,2]\
		+img[i+1,j-1]*mask_v[2,0]+img[i+1,j]*mask_v[2,1]+img[i+1,j+1]*mask_v[2,2]
		sobel_y= img[i-1,j-1]*mask_h[0,0]+img[i-1,j]*mask_h[0,1]+img[i-1,j+1]*mask_h[0,2]\
		+img[i,j-1]*mask_h[1,0]+img[i,j]*mask_h[1,1]+img[i,j+1]*mask_h[1,2]\
		+img[i+1,j-1]*mask_h[2,0]+img[i+1,j]*mask_h[2,1]+img[i+1,j+1]*mask_h[2,2]
		img_new[i,j]=min(255,np.sqrt(sobel_x**2+sobel_y**2))
img_new = img_new.astype(np.uint8)
cv2.imshow("Old Picture", img)
cv2.imshow("New Picture", img_new)
cv2.waitKey(0)
