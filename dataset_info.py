import os

# Dataset location
base_path = "dataset/chest_xray"

folders = ["train", "val", "test"]

for folder in folders:

    print(f"\n===== {folder.upper()} =====")

    folder_path = os.path.join(base_path, folder)

    classes = os.listdir(folder_path)

    for cls in classes:

        class_path = os.path.join(folder_path, cls)

        total_images = len(os.listdir(class_path))

        print(f"{cls} : {total_images} images")