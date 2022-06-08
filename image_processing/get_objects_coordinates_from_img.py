import cv2
import random

def denormalize_pixels(img, label:str):
    size = img.shape
    normalized_values = list(map(float, label.split(" ")))

    x=int(size[0]*(normalized_values[1] - random.randrange(0, 2)* normalized_values[3]/2.0))
    y=int(size[1]*(normalized_values[2] - random.randrange(0, 2)* normalized_values[4]/2.0))
    # x=int(size[0]*(normalized_values[1]))
    # y=int(size[1]*(normalized_values[2]))
    width=int(size[0]*normalized_values[3])
    height=int(size[1]*normalized_values[4])
    return {"x": x,"y":y, "width":width,"height":height}

def get_all_labels(labelPath):
    file = open(labelPath)
    lines = file.readlines()
    return lines

def get_objects_coordinates_from_img(img,label):
    img =cv2.imread(img)
    labels = get_all_labels(label)
    denormalizedLabels = []
    for label in labels:
        if not ( label[0] == "0"): #skip arrows
            denormalizedLabels.append(denormalize_pixels(img,label))
    print(denormalizedLabels)
    return denormalizedLabels
