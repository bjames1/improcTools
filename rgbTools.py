################################################################################
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
import numpy as np
import glob, cv2, os
from PIL import Image
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
grayScale = False;
changeRGBs = False;
rmForeground = True;
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
# Get all images as a list in the current directory.
imgs = glob.glob('./*.png');
imgs.sort();
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
# green html code "00ff00"
#------------------------------------------------------------------------------#
# Grayscale images
if grayScale == True:
    try:
        dir = './grays/';
        os.makedirs(dir)
        for path in imgs:
            img = cv2.imread(path);
            # cv2.imshow('img', img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
            # cv2.imshow('gray', gray)
            path = path.replace('./', './grays/');
            cv2.imwrite(path, gray);
    except:
        print('done')
#------------------------------------------------------------------------------#
# green html code "00ff00"
#------------------------------------------------------------------------------#
import numpy as np
import glob
from PIL import Image

if changeRGBs == True:
    try:
        dir = './bbgs/';
        os.makedirs(dir)
        for path in imgs:

            # Open image and make RGB and HSV versions
            RGBim = Image.open(path).convert('RGB')
            HSVim = RGBim.convert('HSV')

            # Make numpy versions
            RGBna = np.array(RGBim)
            HSVna = np.array(HSVim)

            # Extract Hue
            H = HSVna[:,:,0]

            # Find all green pixels, i.e. where 100 < Hue < 140
            lo,hi = 100,140
            # Rescale to 0-255, rather than 0-360 because we are using uint8
            lo = int((lo * 255) / 360)
            hi = int((hi * 255) / 360)
            green = np.where((H>lo) & (H<hi))

            # Make all green pixels black in original image
            RGBna[green] = [0,0,0]


            count = green[0].size
            print("Pixels matched: {}".format(count))


            path = path.replace('./', './bbgs/');

            Image.fromarray(RGBna).save(path)

    except:
        print('done')
#------------------------------------------------------------------------------#
if rmForeground == True:

    imgs = glob.glob('./bbgs/*.png');
    imgs.sort();

    try:

        dir = './noFGs/';
        os.makedirs(dir)

        for path in imgs:

            img = cv2.imread(path,0)
            ret,th1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY)

            # Create an empty skeleton
            size = np.size(th1)
            skel = np.zeros(th1.shape, np.uint8)

            # Get a Cross Shaped Kernel
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

            closing = cv2.morphologyEx(th1, cv2.MORPH_CLOSE, kernel)

            path = path.replace('./bbgs/', './noFGs/');
            cv2.imwrite(path, closing);

    except:
        print('done')
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
################################################################################
