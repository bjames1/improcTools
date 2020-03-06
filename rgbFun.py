# RGB channel manipulation

img = cv2.imread(imgs[0], cv2.IMREAD_UNCHANGED);
# cv2.imshow('img', img);

b = img.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0

g = img.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = img.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0


# RGB - Blue
# cv2.imshow('B-RGB', b)

# RGB - Green
# cv2.imshow('G-RGB', g)

# RGB - Red
# cv2.imshow('R-RGB', r)


#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
cv2.waitKey(0)
cv2.destroyAllWindows()
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
