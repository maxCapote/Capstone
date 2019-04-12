from PIL import Image
import os
import time

# 1024 x 768
img = Image.new('RGB', (4096, 3072), (153, 51, 255))
print("creating...")
img.save('test.png')
"""
time.sleep(5)
print("deleting...")
os.remove('red.png')

def main():
    try:
        #Relative Path 
        img = Image.open("osrs.png")
          
        #Angle given 
        img = img.rotate(180)  
          
         #Saved in the same relative location 
        img.save("rotated_picture.png") 
    except IOError: 
        pass
  
if __name__ == "__main__": 
    main()
"""