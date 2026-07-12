import questionary
from enum import Enum
from PIL import Image
from pathlib import Path
from constants import LOW, MEDIUM, HIGH, LOSSLESS, JPG, PNG, GIF, YES, NO
from resize_image import resize_img


def convert_img(src_dir, dest_dir):

    class Quality(Enum):
        LOW = "Low"
        MEDIUM = "Medium"
        HIGH = "High"
        LOSSLESS = "Lossless"

    quality_choice = questionary.select(
        "Please select your preferred compression quality: ",
        choices=[
            questionary.Choice(Quality.LOW.value, value=LOW),
            questionary.Choice(Quality.MEDIUM.value, value=MEDIUM),
            questionary.Choice(Quality.HIGH.value, value=HIGH),
            questionary.Choice(Quality.LOSSLESS.value, value=LOSSLESS),
        ],
    ).ask()

    if quality_choice == LOSSLESS:
        is_lossless = True
    else:
        is_lossless = False

    rename_choice = questionary.select(
        "Whould you like to rename your images: ",
        choices=[YES, NO],
    ).ask()

    if rename_choice == YES:
        file_number = 0
        custom_file_name = questionary.text(
            "Please enter your preferred naming convention"
        ).ask()

    for img_file in src_dir.iterdir():
        if (
            img_file.is_file()
            and img_file.name.endswith((JPG, PNG, GIF))
            and not img_file.name.startswith(".")
        ):
            current_img_path = src_dir / img_file.name

            with Image.open(current_img_path) as current_img:

                resized_img = resize_img(current_img)

                if rename_choice == YES:
                    file_number += 1
                    file_name = f"{custom_file_name}_{file_number:02d}"
                    resized_img.save(
                        f"{dest_dir}/{file_name}.webp",
                        format="WEBP",
                        lossless=is_lossless,
                        quality=quality_choice,
                    )
                elif rename_choice == NO:
                    file_name = Path(current_img.filename).stem
                    resized_img.save(
                        f"{dest_dir}/{file_name}.webp",
                        format="WEBP",
                        lossless=is_lossless,
                        quality=quality_choice,
                    )
