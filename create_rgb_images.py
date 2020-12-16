import os
from imutils import paths
import shutil

def create_rgb_images():
    root_dir = "F:/Program Files/feiq/Recv Files/2020_12"
    des_dir="F:/Program Files/feiq/Recv Files/2020_12_RGB"
    images = paths.list_images(root_dir, contains="RGB")
    for i, image_path in enumerate(images):
        print(i, image_path)

        shutil.copy(image_path,des_dir)



if __name__ == '__main__':
    create_rgb_images()
