import os
from ursina import load_texture

block_textures = []

MAP_SIZE = 20
BASE_DIR = os.getcwd()
BLOCKS_DIR  = os.path.join(BASE_DIR, 'assets/blocks')

file_list = os.listdir(BLOCKS_DIR)

for image in file_list:
    texture = load_texture('assets/blocks' + os.sep + image)
    block_textures.append(texture)