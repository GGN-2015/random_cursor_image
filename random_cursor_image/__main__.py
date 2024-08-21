from .img_creator import random_cursor_image
import json
import time
import sys



def main():
    sys_argv = json.loads(json.dumps(sys.argv[1:]))

    if len(sys_argv) not in [1, 3]:

        raise AssertionError("argv length incorrect.")
    if len(sys_argv) == 1: # usage1: python3 -m random_cursor_image <IMAGE_SAVE_PATH>
        save_path = sys_argv[0]
        random_cursor_image(int(time.time() * (10**6)), save_path)
        exit(0)

    if len(sys_argv) == 3: # usage2: python3 -m random_cursor_image -r <RANDOM_SEED> <IMAGE_SAVE_PATH>
        if sys_argv[0] != "-r":
            raise AssertionError("first argv must be '-r'.")
        random_seed = int(sys_argv[1])
        save_path   = sys_argv[2]
        random_cursor_image(random_seed, save_path)
        exit(0)

    raise AssertionError("unimplemented.")



if __name__ == "__main__":
    main()