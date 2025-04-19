import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['08.png', '09.png']
images = []

# Set the size to which all images will be resized
target_size = (300, 300)  # Change as needed

for filename in filenames:
    img = Image.open(filename).convert("RGB")  # Ensure consistent format
    img = img.resize(target_size)
    images.append(np.array(img))

iio.imwrite('team.gif', images, duration=500, loop=0)
print("GIF created successfully!")
