import questionary
from pathlib import Path
from constants import DEST_FOLDER
from convert_image import convert_img


def main():

    src_dir_path = questionary.path(
        "Please enter the absolute path to the folder containing the original images: "
    ).ask()

    src_dir = Path(src_dir_path)
    dest_dir = src_dir / DEST_FOLDER

    dest_dir.mkdir(parents=True, exist_ok=True)

    convert_img(src_dir, dest_dir)


if __name__ == "__main__":
    main()
