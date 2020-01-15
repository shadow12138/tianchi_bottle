from yolo import YOLO
from PIL import Image
import os
import random


def save_result():
    yolo = YOLO()
    images = []
    annotations = []
    for index, image_path in enumerate(os.listdir('testing_images')):
        print(index)
        image = Image.open('testing_images/' + image_path)
        image_id = index + 1
        image, curr = yolo.my_detect_image(image, image_id)
        images.append({
            'id': image_id,
            'file_name': image_path
        })
        annotations.extend(curr)
    my_result = {'images': images, 'annotations': annotations}
    result = open('my_result.json', 'w')
    result.write(str(my_result).replace('\'', '\"'))
    result.close()


def show_result():
    yolo = YOLO()
    images = os.listdir('testing_images')

    for i in range(20):
        index = random.randint(0, len(images))
        image = Image.open('testing_images/' + images[index])
        yolo.detect_image(image)
        image.show()


if __name__ == '__main__':
    # show_result()
    save_result()
