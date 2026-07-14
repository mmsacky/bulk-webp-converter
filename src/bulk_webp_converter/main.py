import questionary, time
from rich.console import Console
from pathlib import Path
from .constants import DEST_FOLDER
from .convert_image import convert_img
from .check_directory import has_no_valid_images, create_destination_directory

console = Console()


def main():

    console.print("[bold cyan]🤖 Starting batch image processor...[/bold cyan]")
    time.sleep(0.8)

    src_dir_path = questionary.path(
        "Please enter the absolute path to the folder containing the original images: "
    ).ask()

    src_dir = Path(src_dir_path)

    try:

        if not has_no_valid_images(src_dir):
            dest_dir = src_dir / DEST_FOLDER
            create_destination_directory(dest_dir)
        else:
            console.print(
                "[bold red]Error encountered: Folder has no valid images[/bold red]"
            )
            return

    except NotADirectoryError as e:
        console.print(f"[bold red]Error encountered: {e} [/bold red]")
        return

    time.sleep(0.8)

    convert_img(src_dir, dest_dir)

    time.sleep(0.8)

    console.print(
        "\n[bold green]✔ All images converted to WebP successfully![/bold green]"
    )


if __name__ == "__main__":
    main()
