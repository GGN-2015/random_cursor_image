import os
from tqdm import tqdm
import sys
import random
import math
from PIL import Image
DIRNOW = os.path.dirname(os.path.abspath(__file__))



BACKGROUND_COLOR   = (128, 128, 128, 0xff)
SMALL_CURSOR_CNT   = 600
SMALL_CURSOR_SIZE  = 30
LARGE_CURSOR_CNT   = 50
LARGE_CURSOR_SIZE  = 240
MEDIUM_CURSOR_CNT  = round(math.sqrt(SMALL_CURSOR_CNT  * LARGE_CURSOR_CNT))
MEDIUM_CURSOR_SIZE = round(math.sqrt(SMALL_CURSOR_SIZE * LARGE_CURSOR_SIZE))



def get_cursor_png(cursor_png_path: str):
    return Image.open(cursor_png_path).convert("RGBA")



def put_cursor_on_pos(image_size, cursor_png_path, old_image, px, py, cursor_width):
    cursor = get_cursor_png(cursor_png_path)
    w, h = cursor.size
    cursor = cursor.resize((cursor_width, round(h/w*cursor_width)))
    new_image = Image.new("RGBA", image_size, (0xff, 0xff, 0xff, 0x00))
    new_image.paste(cursor, (px, py))
    return Image.alpha_composite(old_image, new_image)



def put_cursor(image_size, cursor_png_path, image, cursor_size: int, cursor_cnt: int):
    for _ in tqdm(range(cursor_cnt)):
        px = random.randint(0, image_size[0] - 1)
        py = random.randint(0, image_size[1] - 1)
        image = put_cursor_on_pos(image_size, cursor_png_path, image, px, py, cursor_size)
    return image



def make_image(image_size, cursor_png_path: str, savepath: str):
    image = Image.new("RGBA", image_size, BACKGROUND_COLOR)

    sys.stderr.write("\033[1;32mINFO\033[0m: rendering small cursors.\n")
    image = put_cursor(image_size, cursor_png_path, image,  SMALL_CURSOR_SIZE,  SMALL_CURSOR_CNT)

    sys.stderr.write("\033[1;32mINFO\033[0m: rendering medium cursors.\n")
    image = put_cursor(image_size, cursor_png_path, image, MEDIUM_CURSOR_SIZE, MEDIUM_CURSOR_CNT)

    sys.stderr.write("\033[1;32mINFO\033[0m: rendering large cursors.\n")
    image = put_cursor(image_size, cursor_png_path, image,  LARGE_CURSOR_SIZE,  LARGE_CURSOR_CNT)
    image.save(savepath)



def random_cursor_image(random_seed:int, save_path:str, cursor_png_path=None, image_size=(1920, 1080)):
    if random_seed is not None: # set random seed
        random.seed(random_seed)
    if cursor_png_path is None: # default cursor image
        cursor_png_path = os.path.join(DIRNOW, "img", "cursor.png")
    assert os.path.isfile(cursor_png_path)
    make_image(image_size, cursor_png_path, save_path)
