import cv2
import imutils
from imutils import paths

image_counter = 0
ws=1000
step=800
image_path="Full Drawings"
#output_path="cropped_image"

for i in paths.list_images(image_path):

	img = cv2.imread(i, cv2.IMREAD_UNCHANGED)

	h,w = img.shape[:2]
	print(h,w)

	for i in range(0,h-ws,step):
		for j in range(0,w-ws,step):
			crop_image = img[i:i+ws,j:j+ws]
			image_name = "cropped_image\\"+str(image_counter)+".jpg"
			cv2.imwrite(image_name,crop_image)
			image_counter+=1

#resized = imutils.resize(img, width=4000)
#img=cv2.resize(img,(000,2000))
cv2.imshow("output",img)
#cv2.imwrite("res.jpg",img)
cv2.waitKey(0)
#print(resized.shape)
