import cv2
import os

from process_image import process_images_from_path

def __ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def __save_image(img, outputPath):
    __ensure_dir(outputPath)
    cv2.imwrite(outputPath,img)



def save_imgs_from_path(path, output_path,processFn): 
    processed_imgs = processFn(path)
    i = 0
    for img in processed_imgs:
        i = i + 1
        __save_image(img,os.path.join(os.getcwd(), output_path, str(i) +  '.jpg'))


save_imgs_from_path('imgs', 'converted_imgs', process_images_from_path)