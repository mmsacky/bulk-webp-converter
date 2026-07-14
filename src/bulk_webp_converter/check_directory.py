from .constants import JPG, PNG, GIF, DEST_FOLDER
from rich.console import Console

console = Console()


def has_no_valid_images(src_dir):

    if not src_dir.is_dir():
        raise NotADirectoryError(f"{src_dir} is not a valid directory.")

    valid_formats = [JPG, PNG, GIF]

    for item in src_dir.iterdir():
        if item.is_file() and item.suffix.lower() in valid_formats:
            return False
    return True


def create_destination_directory(dest_dir):
    try:
        dest_dir.mkdir(parents=True, exist_ok=False)
        console.print(
            f"[bold cyan]Creating the {DEST_FOLDER} folder in the source directory...[/bold cyan]"
        )

    except FileExistsError:
        console.print(
            f"[bold green]Using {DEST_FOLDER} as the destination folder...[/bold green]"
        )
    except PermissionError:
        console.print(
            f"[bold red] Cannot create {DEST_FOLDER}. Check your permissions for parent folder...[/bold red]"
        )
