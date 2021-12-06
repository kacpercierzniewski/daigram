import numpy as np
import cv2
from os import walk, path, getcwd

def __dilateImage(img):
    kernel = np.ones((5,5))
    return cv2.dilate(img, kernel, iterations=1)

def process_image(source):
    imgBlur = cv2.GaussianBlur(source, (7,7),1)
    imgGrayBlur = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos("Threshold1", "Thresholds")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Thresholds")
    print(threshold1)
    print(threshold2)
    return __dilateImage(cv2.Canny(imgGrayBlur,threshold1 if threshold1 != -1 else 92, threshold2 if threshold2 != -1 else 0))

def get_all_files_paths_from_folder(folder_path):
    absolute_path = path.join(getcwd(), folder_path)
    f= []
    for (dirpath,_, filenames) in walk(absolute_path): 
        for filename in filenames:
            f.append(path.join(dirpath,filename))
        break
    return f

def process_images_from_path(path):
    imgs_paths = get_all_files_paths_from_folder('imgs')
    processed_imgs = []
    for path in imgs_paths:
        processed_imgs.append(process_image(cv2.imread(path)))
    return processed_imgs




print(process_images_from_path('imgs'))