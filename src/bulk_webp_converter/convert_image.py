import questionary, time
from rich.console import Console
from rich.progress import track
from enum import Enum
from PIL import Image, UnidentifiedImageError
from pathlib import Path
from .constants import LOW, MEDIUM, HIGH, LOSSLESS, JPG, PNG, GIF, YES, NO
from .resize_image import resize_img
from .key_binding import quality_key_bind

console = Console()


class Quality(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    LOSSLESS = "Lossless"
    CUSTOM = "Custom"


def convert_img(src_dir, dest_dir):

    quality_choice = questionary.select(
        "Please select your preferred compression quality: ",
        choices=[
            questionary.Choice(Quality.LOW.value, value=LOW),
            questionary.Choice(Quality.MEDIUM.value, value=MEDIUM),
            questionary.Choice(Quality.HIGH.value, value=HIGH),
            questionary.Choice(Quality.LOSSLESS.value, value=LOSSLESS),
            questionary.Choice(Quality.CUSTOM.value),
        ],
    ).ask()

    time.sleep(0.8)

    if quality_choice == Quality.CUSTOM.value:
        custom_quality = questionary.text(
            "Enter a number from 1 to 100 (non-numbers are locked): ",
            key_bindings=quality_key_bind,
        ).ask()
        quality_choice = int(custom_quality)
        is_lossless = False
    elif quality_choice == LOSSLESS:
        is_lossless = True
    else:
        is_lossless = False

    rename_choice = questionary.select(
        "Would you like to rename your images: ",
        choices=[YES, NO],
    ).ask()

    time.sleep(0.8)

    if rename_choice == YES:
        file_number = 0
        custom_file_name = questionary.text(
            "Please enter your preferred naming convention"
        ).ask()

    for img_file in track(
        src_dir.iterdir(), description="[bold yellow]Processing images...[/bold yellow]"
    ):

        if (
            img_file.is_file()
            and img_file.name.lower().endswith((JPG, PNG, GIF))
            and not img_file.name.startswith(".")
        ):

            current_img_path = src_dir / img_file.name

            try:
                with Image.open(current_img_path) as current_img:

                    resized_img = resize_img(current_img)

                    current_img_name = Path(current_img.filename).stem

                    if rename_choice == NO:
                        file_name = current_img_name
                    else:
                        file_number += 1
                        file_name = f"{custom_file_name}_{file_number:02d}"
                        console.print(
                            f"[bold yellow]✍ Renaming[/bold yellow]    | [dim]{current_img_name}[/dim] → [bold white]{file_name}[/bold white]"
                        )

                    console.print(
                        f"[bold blue]⚡ Converting[/bold blue]   | [dim]{file_name}[/dim] to WebP..."
                    )

                    time.sleep(0.5)

                    resized_img.save(
                        f"{dest_dir}/{file_name}.webp",
                        lossless=is_lossless,
                        quality=quality_choice,
                    )
                    console.print(
                        f"[bold green]✔ Success[/bold green]   | Converted [bold white]{file_name}[/bold white]!"
                    )
                    time.sleep(0.5)

            except UnidentifiedImageError:
                console.print(
                    f"[bold red]❌ Error:[/bold red] Failed to open '{img_file.name}' [dim](Corrupt or invalid image)[/dim]"
                )
