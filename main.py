import cv2
source ="img1.jpg"
destination= "newimg.jpeg"
scale_percent=50
src=cv2.imread("img1.jpg",cv2.IMREAD_UNCHANGED)
#cv2.imshow("photo",src)
#percent by which the image is resized


#calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite('newimg.jpeg',output)
#cv2.waitKey(0)