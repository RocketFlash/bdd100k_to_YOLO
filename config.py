owner_prefix = '/home/rauf/'
dataset_path = owner_prefix + 'datasets/bdd100k/'
labels_path = dataset_path + 'labels_bdd100k_format/'
images_path = dataset_path + 'images/'
images_path_train = images_path + 'train/'
images_path_val = images_path + 'val/'
train_labels_json_path = labels_path + 'bdd100k_labels_images_train.json'
val_labels_json_path = labels_path + 'bdd100k_labels_images_val.json'
save_path = dataset_path + 'yolo_files/'
labels_save_path = dataset_path + 'labels/'
labels_save_path_train = labels_save_path + 'train/'
labels_save_path_val = labels_save_path + 'val/'
train_file_path = save_path + 'train.txt'
val_file_path = save_path + 'val.txt'

img_size = (1280, 720)
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

PATHS = {
    'owner_prefix': owner_prefix,
    'dataset_path': dataset_path,
    'labels_path': labels_path,
    'images_path': images_path,
    'images_path_train': images_path_train,
    'images_path_val': images_path_val,
    'train_labels_json_path': train_labels_json_path,
    'val_labels_json_path': val_labels_json_path,
    'train_file_path': train_file_path,
    'val_file_path': val_file_path,
    'save_path': save_path,
    'labels_save_path': labels_save_path,
    'labels_save_path_train': labels_save_path_train,
    'labels_save_path_val': labels_save_path_val
}
