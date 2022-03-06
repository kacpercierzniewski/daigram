from typing import Dict, List, Set
import cv2

from process_image import get_all_files_paths_from_folder



def read_all_imgs_paths():
    return get_all_files_paths_from_folder('imgs/all/images')

def read_all_labels_paths():
    return get_all_files_paths_from_folder('imgs/all/labels')


#todo - this is not needed now, values from folders matches automatically because of the same file names and file count in folders
def match_img_with_labels():  
    return 

def denormalize_pixels(img, label:str):
    size = img.shape
    normalized_values = list(map(float, label.split(" ")))

    x=int(size[0]*(normalized_values[1] - normalized_values[3]/2.0))
    y=int(size[1]*(normalized_values[2] - normalized_values[4]/2.0))
    width=int(size[0]*normalized_values[3])
    height=int(size[1]*normalized_values[4])
    return {x,y, width,height}

def get_all_labels(labelPath):
    file = open(labelPath)
    lines = file.readlines()
    return lines


def get_objects_from_img(img,label):
    img =cv2.imread(img)
    labels = get_all_labels(label)
    denormalizedLabels = []
    for label in labels:
        denormalizedLabels.append(denormalize_pixels(img,label))
    print(denormalizedLabels)
    return

def add_titles_to_shapes():
    img_paths = read_all_imgs_paths()
    label_paths = read_all_labels_paths()

    get_objects_from_img(img_paths[0], label_paths[0])




add_titles_to_shapes()