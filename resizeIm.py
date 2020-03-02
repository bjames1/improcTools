import cv2

filename = 'im.png';
img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ',img.shape)

# scale_percent = 60 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)

width = 440;
height = 440;
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

print('Resized Dimensions : ',resized.shape)

# cv2.imshow("Resized image", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite(filename,resized)
