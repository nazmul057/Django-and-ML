from PIL import Image
import glob
import pandas as pd


#image_list = []

all_heights = []
all_widths = []

for filename in glob.glob(r'D:\D\pneumonia_datasets\chest_xray\P_train\PNEUMONIA\*.jpeg'): #assuming gif
    im=Image.open(filename)

    width, height = im.size

    all_heights.append(height)
    all_widths.append(width)


df_h = pd.DataFrame(all_heights)
df_w = pd.DataFrame(all_widths)

print(df_h.min())
print(df_w.min())

j = 0
for i in all_heights:
    if i == 127:
        break
    else:
        j += 1

print(j)
'''
image_file = "img4.jpeg"
img = Image.open(image_file)

width, height = img.size

print(height, width)
'''