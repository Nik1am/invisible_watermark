from PIL import Image
import sys

secret_image = "k.png"

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = "1.png"
img = Image.open(fname).convert("RGB")
secret = Image.open(secret_image).convert("RGB").resize(img.size)
channels = tuple(secret.split())
channels2 = []
for i,c in enumerate(channels):
  channels2.append(c.convert("1").convert("L"))

secret_data = list(Image.merge("RGB",channels2).getdata())
data = list(img.getdata())
newdata = []

def a(b):
    if b > 127:
        return "1"
    return "0"

for i,px in enumerate(data):
    px2 = [int(format(c, '08b')[0:7]+a(secret_data[i][j]),2) for j,c in enumerate(px)]
    newdata.append(tuple(px2))

im2 = img.copy()
im2.putdata(newdata)
im2.save("signed.png")