from .img_creator import random_cursor_image
import os

def main():
    dirnow = os.path.dirname(os.path.abspath(__file__))
    savepath = os.path.join(dirnow, "..", "sample_image.png")
    random_cursor_image(1145141919810, savepath)

if __name__ == "__main__":
    main()