import json


def generate_yolo_annotation():
    file = open('annotations.json', 'r')
    content = file.read()
    json_obj = json.loads(content)
    image_dict = {}
    for image_obj in json_obj['images']:
        image_dict[image_obj['id']] = {
            'file_name': image_obj['file_name'],
            'height': image_obj['height'],
            'width': image_obj['width']
        }

    my_annotation = open('yolo_train.txt', 'w')
    for i_id in image_dict:
        image = image_dict[i_id]
        annotations = []
        for annotation in json_obj['annotations']:
            if annotation['image_id'] == i_id:
                x, y, w, h = map(int, annotation['bbox'])
                x1, y1, x2, y2 = x, y, x + w, y + h
                cls_id = int(annotation['category_id'])
                if cls_id == 0: continue
                annotations.append(' %d,%d,%d,%d,%s' % (x1, y1, x2, y2, cls_id - 1))
        if len(annotations) > 0:
            my_annotation.write('training_images/%s' % (image['file_name']))
            for annotation in annotations:
                my_annotation.write(annotation)
            my_annotation.write('\n')
    my_annotation.close()

    class_mapping = {}
    for category in json_obj['categories']:
        key = int(category['id'])
        if key == 0:
            continue
        class_mapping[key - 1] = category['name']
    for category in sorted(class_mapping):
        print(class_mapping[category])
    file.close()


if __name__ == '__main__':
    generate_yolo_annotation()
