import json
import os
from tqdm import tqdm


def generate_yolo_labels(json_path, save_path, categories, img_size, is_train=True, with_fake=True):
    img_w, img_h = img_size
    with open(json_path) as json_file:
        data = json.load(json_file)
        print('Start bdd100k to YOLO labels conversion')
        print('Total number of files: {}'.format(len(data)))
        for img in tqdm(data):
            img_name = img['name']
            img_label_txt = str(img_name[:-4]) + ".txt"
            img_label_txt_fake = str(img_name[:-4]) + "_fake_B.txt"
            img_labels = [l for l in img['labels']
                          if l['category'] not in ignore_categories]
            file_path = save_path + 'original_day/' + \
                ('train_' if is_train else 'val_') + img_label_txt
            file_path_fake = save_path + 'fake_night/' + \
                ('train_' if is_train else 'val_') + img_label_txt_fake
            with open(file_path, 'w+') as f_label, open(file_path_fake, 'w+') as f_label_fake:
                for label in img_labels:
                    y1 = label['box2d']['y1']
                    x2 = label['box2d']['x2']
                    x1 = label['box2d']['x1']
                    y2 = label['box2d']['y2']
                    class_name = label['category']
                    class_id = categories[class_name]

                    bbox_x = (x1 + x2)/2
                    bbox_y = (y1 + y2)/2

                    bbox_width = x2-x1
                    bbox_height = y2-y1

                    bbox_x_norm = bbox_x / img_w
                    bbox_y_norm = bbox_y / img_h

                    bbox_width_norm = bbox_width / img_w
                    bbox_height_norm = bbox_height / img_h

                    line_to_write = '{} {} {} {} {}'.format(
                        class_id, bbox_x_norm, bbox_y_norm, bbox_width_norm, bbox_height_norm)
                    f_label.write(line_to_write + "\n")
                    if with_fake:
                        f_label_fake.write(line_to_write + "\n")


def generate_yolo_filenames(imgs_path, output_file_path, owner_prefix=None, img_start_prefix=None, exclude=[]):
    print('Start YOLO filenames file creation')
    if owner_prefix is None:
        owner_prefix = '/home/'+os.getlogin()+'/'
    with open(output_file_path, 'w+') as f:
        for dirpath, dirs, files in os.walk(imgs_path):
            dirs[:] = [d for d in dirs if d not in exclude]
            for filename in files:
                file_path = os.path.join(owner_prefix, dirpath, filename)
                if filename.endswith(".jpg"):
                    if img_start_prefix is not None:
                        if filename.startswith(img_start_prefix):
                            f.write(file_path + "\n")
                    else:
                        f.write(file_path + "\n")


if __name__ == '__main__':
    categories = {'car': 0,
                  'bus': 1,
                  'person': 2,
                  'bike': 3,
                  'truck': 4,
                  'motor': 5,
                  'train': 6,
                  'rider': 7,
                  'traffic sign': 8,
                  'traffic light': 9}
    dataset_path = 'datasets/bdd100k/'
    labels_path = dataset_path + 'labels/'
    images_path = dataset_path + 'images/'
    train_labels_json_path = labels_path + 'bdd100k_labels_images_train.json'
    val_labels_json_path = labels_path + 'bdd100k_labels_images_val.json'
    save_path = dataset_path + 'yolo_files/labels/'
    ignore_categories = ["drivable area", "lane"]
    img_size = (1280, 720)

    generate_yolo_labels(train_labels_json_path, save_path,
                         categories, img_size, is_train=True, with_fake=True)
    generate_yolo_labels(val_labels_json_path, save_path,
                         categories, img_size, is_train=False, with_fake=True)

    with_fake_night = False
    save_path = dataset_path + 'yolo_files/' + \
        ('with_fake/' if with_fake_night else 'without_fake/')
    train_file_path = save_path + 'train.txt'
    val_file_path = save_path + 'val.txt'
    exclude = [] if with_fake_night else ['fake_night']

    generate_yolo_filenames(images_path, train_file_path,
                            img_start_prefix='train_', exclude=exclude)
    generate_yolo_filenames(images_path, val_file_path,
                            img_start_prefix='val_', exclude=exclude)
