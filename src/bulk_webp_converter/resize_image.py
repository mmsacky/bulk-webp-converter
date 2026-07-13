from PIL import Image
from pathlib import Path
from rich.console import Console
from constants import LS_MAX_WIDTH, PORT_MAX_WIDTH, SQ_MAX_WIDTH


def resize_img(image):

    console = Console()
    file_name = Path(image.filename).stem

    aspect_ratio = image.height / image.width

    if image.width > image.height and image.width > LS_MAX_WIDTH:
        console.log(
            f"[bold cyan]↔ Landscape[/bold cyan] | Resizing [dim]{file_name}[/dim]..."
        )
        proportional_height = aspect_ratio * LS_MAX_WIDTH
        processed_image = image.resize(
            (LS_MAX_WIDTH, round(proportional_height)),
            resample=Image.Resampling.LANCZOS,
        )
        console.log(
            f"[bold green]✔ Success[/bold green]   | Resized [dim]{file_name}[/dim]"
        )

    elif image.width < image.height and image.width > PORT_MAX_WIDTH:
        console.log(
            f"[bold purple]↕ Portrait[/bold purple]  | Resizing [dim]{file_name}[/dim]..."
        )
        proportional_height = aspect_ratio * PORT_MAX_WIDTH
        processed_image = image.resize(
            (PORT_MAX_WIDTH, round(proportional_height)),
            resample=Image.Resampling.LANCZOS,
        )
        console.log(
            f"[bold green]✔ Success[/bold green]   | Resized [dim]{file_name}[/dim]"
        )

    elif image.width == image.height and image.width > SQ_MAX_WIDTH:
        console.log(
            f"[bold yellow]⬜ Square[/bold yellow]    | Resizing [dim]{file_name}[/dim]..."
        )
        processed_image = image.resize(
            (SQ_MAX_WIDTH, SQ_MAX_WIDTH), resample=Image.Resampling.LANCZOS
        )
        console.log(
            f"[bold green]✔ Success[/bold green]   | Resized [dim]{file_name}[/dim]"
        )

    else:
        return image

    return processed_image
