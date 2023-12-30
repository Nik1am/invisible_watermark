from PIL import Image
import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = "signed.png"
img = Image.open(fname)
data = list(img.getdata())
newdata = []
for px in data:
    px2 = [int(format(c, '08b')[-1])*255 for c in px]
    newdata.append(tuple(px2))

im2 = img.copy()
im2.putdata(newdata)
im2.convert("P", palette = Image.ADAPTIVE, colors = 8).save("dec.png")