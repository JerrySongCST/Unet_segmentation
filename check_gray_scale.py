import cv2

img_route = r'E:\Projects\Cephalometry\data\all_data\31-30-0109.jpeg'


image1 = cv2.imread(img_route)

cv2.imwrite('imgR.jpg', image1[:, :, 0])
cv2.imwrite('imgG.jpg', image1[:, :, 1])
cv2.imwrite('imgB.jpg', image1[:, :, 2])