import questionary, time
from rich.console import Console
from pathlib import Path
from constants import DEST_FOLDER
from convert_image import convert_img


def main():
    console = Console()
    console.print("[bold cyan]🤖 Starting batch image processor...[/bold cyan]")
    time.sleep(0.8)

    src_dir_path = questionary.path(
        "Please enter the absolute path to the folder containing the original images: "
    ).ask()

    src_dir = Path(src_dir_path)
    dest_dir = src_dir / DEST_FOLDER

    dest_dir.mkdir(parents=True, exist_ok=True)

    time.sleep(0.8)

    convert_img(src_dir, dest_dir)

    time.sleep(0.8)

    console.print(
        "\n[bold green]✔ All images converted to WebP successfully![/bold green]"
    )


if __name__ == "__main__":
    main()
