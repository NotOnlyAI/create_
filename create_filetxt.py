
from imutils import paths
def create_filetxt():
    root_dir="F:/Program Files/feiq/Recv Files/2020_12_RGB"
    images = paths.list_images(root_dir, contains="RGB")
    with open("images.txt","w") as fileimage:

        for i, image_path in enumerate(images):

            image_name=image_path.split("\\")[-1]
            print(i,image_name)
            fileimage.write(image_name)
            fileimage.write("\n")


if __name__ == '__main__':
    create_filetxt()