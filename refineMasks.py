#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import glob, os
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
binCircle = Image.new("L", (440, 440), 0)
x, y =  binCircle.size
eX, eY = (352, 352) #Size of Bounding Box for ellipse
bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
draw = ImageDraw.Draw(binCircle)
draw.ellipse(bbox, fill=256)
del draw
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
shined = glob.glob('./shined/*.png');
shined.sort();

masks = glob.glob('./noFGs/*.png');
masks.sort();
#------------------------------------------------------------------------------#
try:

    dir = './refined/';
    os.makedirs(dir)

    for i in range(len(shined)):

        fgPath=shined[i];
        fgMask=masks[i];

        fg = Image.open(fgPath);
        fg = fg.resize((440, 440))
        # fg.show()

        bg = Image.new("L", fg.size, 130);
        # bg.show()

        fg_mask = Image.open(fgMask).convert('L').resize(fg.size);
        # fg_mask.show()

        comp1 = Image.composite(fg, bg, fg_mask);
        # comp1.show()

        gwindow_mask = binCircle;

        gwindow_mask_blurred = gwindow_mask.filter(ImageFilter.GaussianBlur(88));
        # gwindow_mask_blurred.show()

        comp2 = Image.composite(comp1, bg, gwindow_mask_blurred);

        fgPath = fgPath.replace('_LCMatched.png', '');
        fgPath = fgPath.replace('./shined/', './refined/');

        comp2 = comp2.save(fgPath);

except:
    print('done')
