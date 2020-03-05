from PIL import Image, ImageDraw, ImageFilter

fg = Image.open('gloss_001.png');
# im.show()

bg = Image.new("L", fg.size, 130);
# bg.show()

fg_mask = Image.open('new_mask.png').convert('L').resize(fg.size);
# fg_mask.show()

comp1 = Image.composite(fg, bg, fg_mask);
# comp1.show()

gwindow_mask = Image.open('circ_mask.png').convert('L').resize(fg.size);
# gwindow_mask.show()

gwindow_mask_blurred = gwindow_mask.filter(ImageFilter.GaussianBlur(88))
# gwindow_mask_blurred.show()

comp2 = Image.composite(comp1, bg, gwindow_mask_blurred)
# comp2.show()
