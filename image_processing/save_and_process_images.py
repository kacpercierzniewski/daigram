import cv2
import os

def __ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def __save_image(img, outputPath):
    __ensure_dir(outputPath)
    cv2.imwrite(outputPath,img)



def save_and_process_imgs(path, output_path,processFn): 
    processed_imgs = processFn(path)
    i = 0
    for img in processed_imgs:
        i = i + 1
        __save_image(img,os.path.join(os.getcwd(), output_path, str(i) +  '.jpg'))
