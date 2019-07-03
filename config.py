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
owner_prefix = '/home/rauf/'
dataset_path = owner_prefix + 'datasets/bdd100k/'
labels_path = dataset_path + 'labels/'
images_path = dataset_path + 'images/'
train_labels_json_path = labels_path + 'bdd100k_labels_images_train.json'
val_labels_json_path = labels_path + 'bdd100k_labels_images_val.json'
save_path = dataset_path + 'yolo_files/labels/'
img_size = (1280, 720)
