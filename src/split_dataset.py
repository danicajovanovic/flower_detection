from pathlib import Path
import random
import shutil


SOURCE_IMAGES = Path("data/all/images")
SOURCE_LABELS = Path("data/all/labels")

OUTPUT_DIR = Path("data")

TRAIN_RATIO = 0.7
VALID_RATIO = 0.2

IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]


def clear_folder(folder_path):
    folder_path.mkdir(parents=True, exist_ok=True)
    for file in folder_path.iterdir():
        if file.is_file():
            file.unlink()


def prepare_output_folders():
    for split in ["train", "valid", "test"]:
        clear_folder(OUTPUT_DIR / split / "images")
        clear_folder(OUTPUT_DIR / split / "labels")


def get_image_files():
    images = []

    for image_path in SOURCE_IMAGES.iterdir():
        if image_path.suffix.lower() in IMAGE_EXTENSIONS:
            label_path = SOURCE_LABELS / f"{image_path.stem}.txt"

            if label_path.exists():
                images.append(image_path)
            else:
                print(f"Upozorenje: nema label fajla za {image_path.name}")

    return images


def copy_image_and_label(image_path, split_name):
    label_path = SOURCE_LABELS / f"{image_path.stem}.txt"

    shutil.copy2(image_path, OUTPUT_DIR / split_name / "images" / image_path.name)
    shutil.copy2(label_path, OUTPUT_DIR / split_name / "labels" / label_path.name)


def main():
    random.seed(42)

    prepare_output_folders()

    images = get_image_files()
    random.shuffle(images)

    total = len(images)

    train_end = int(total * TRAIN_RATIO)
    valid_end = train_end + int(total * VALID_RATIO)

    train_images = images[:train_end]
    valid_images = images[train_end:valid_end]
    test_images = images[valid_end:]

    for image in train_images:
        copy_image_and_label(image, "train")

    for image in valid_images:
        copy_image_and_label(image, "valid")

    for image in test_images:
        copy_image_and_label(image, "test")

    print("Dataset je uspešno podeljen.")
    print(f"Ukupno slika: {total}")
    print(f"Train: {len(train_images)}")
    print(f"Valid: {len(valid_images)}")
    print(f"Test: {len(test_images)}")


if __name__ == "__main__":
    main()