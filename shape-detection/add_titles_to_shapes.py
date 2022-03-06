import cv2

from process_image import get_all_files_paths_from_folder
from save_images import save_imgs_from_path
import random
import string 
font_list = [cv2.FONT_HERSHEY_COMPLEX, cv2.FONT_HERSHEY_COMPLEX_SMALL, cv2.FONT_HERSHEY_DUPLEX, cv2.FONT_HERSHEY_PLAIN, cv2.FONT_HERSHEY_SCRIPT_COMPLEX, cv2.FONT_HERSHEY_SIMPLEX, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, cv2.FONT_ITALIC]


PATH = 'imgs/all'

def read_all_imgs_paths(path):
    return get_all_files_paths_from_folder(path + '/images')

def read_all_labels_paths(path):
    return get_all_files_paths_from_folder(path + '/labels')


#todo - this is not needed now, values from folders matches automatically because of the same file names and file count in folders
def match_img_with_labels():  
    return 

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
    return denormalizedLabels

def add_titles_to_shapes(path):
    img_paths = read_all_imgs_paths(path)
    label_paths = read_all_labels_paths(path)
    processed_imgs = []

    for i in range(len(img_paths)):
        coords = get_objects_coordinates_from_img(img_paths[i], label_paths[i])
        img = cv2.imread(img_paths[i])
        for coord in coords:
            img = cv2.putText(img,generate_random_text(), (coord["x"], coord["y"]),random.choice(font_list), random.random()/2,(255,255,255) )
        processed_imgs.append(img)
    return processed_imgs

def generate_random_text():
    letters = string.ascii_letters
    result = ''
    for i in range (random.randint(1,6)):
       word = ''.join(random.choice(letters) for i in range(random.randint(1,10)))
       result+= word + " "
    return result


generate_random_text()
# add_titles_to_shapes()

save_imgs_from_path(PATH, PATH+'/processed', add_titles_to_shapes)

