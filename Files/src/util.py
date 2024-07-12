import pygame
import os
from os import walk
# Changes the working directory to the one that we are in, to allow for the paths to be flexible and coherent
os.chdir(os.path.dirname(__file__))

# Function to load an image 
def load_image(path, size):
    
    image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), size)
    
    return image

def load_images(path):
    BASE_PATH = 'Images/'
    surface_list = []

    for _, _, img in walk(path):
        for image in img:
            imagen = pygame.image.load(BASE_PATH + path + image)
            surface_list.append(imagen)


    return surface_list
# Function to return a dictionary with the keys as names of the folders in which the sprites are, and the sprites themselves
# As part of the values of the keys
def load_img_dict(path, size):
    BASE_PATH = 'Images/'

    dictionary = {}

    # Uses the walk method to get the folder's name and list of images inside
    for key_name, _,  img in walk(BASE_PATH + path):
        img_list = []

        # Here I strip the initial character, because then the key's name will end up having the '\' inside of them
        # This way, I ensure that I can have the clean name of the folder
        key_name = key_name.lstrip(BASE_PATH + path)[1:]
        for image in img:
            imagen = pygame.transform.scale(pygame.image.load(BASE_PATH + path + '/' + key_name + '/' + image).convert_alpha(), size)
            img_list.append(imagen)
        dictionary.update({key_name: img_list})


    return dictionary
# Function for rotating an image given a position and an angle
def rotate_img(old_img, topleft, angle):
    center = old_img.get_rect(topleft = topleft).center
    rotated_image = pygame.transform.rotate(old_img, angle)
    new_rect = rotated_image.get_rect(center=center)

    return rotated_image, new_rect


