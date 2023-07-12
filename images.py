from PIL import Image
import asyncio
import os



def is_image(file_path):
    try:
        image = Image.open(file_path)
        image.close()
        return True

    except:
        return False




def grayscale(img):
    image = Image.open(img)
    grayscale_image = image.convert("L")
    filename, extension = os.path.splitext(img)
    new_img = filename + "_grayscale" + extension
    grayscale_image.save(new_img)
    return new_img
    
