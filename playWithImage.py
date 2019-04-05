from PIL import Image
import os
import time

img = Image.new('RGB', (60, 30), color = 'red')
print("creating...")
img.save('red.png')
time.sleep(5)
print("deleting...")
os.remove('red.png')
