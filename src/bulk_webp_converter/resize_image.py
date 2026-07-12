from PIL import Image
from constants import LS_MAX_WIDTH, PORT_MAX_WIDTH, SQ_MAX_WIDTH


def resize_img(image):

    aspect_ratio = image.height / image.width

    if image.width > image.height and image.width > LS_MAX_WIDTH:
        proportional_height = aspect_ratio * LS_MAX_WIDTH
        processed_image = image.resize(
            (LS_MAX_WIDTH, round(proportional_height)),
            resample=Image.Resampling.LANCZOS,
        )

    elif image.width < image.height and image.width > PORT_MAX_WIDTH:
        proportional_height = aspect_ratio * PORT_MAX_WIDTH
        processed_image = image.resize(
            (PORT_MAX_WIDTH, round(proportional_height)),
            resample=Image.Resampling.LANCZOS,
        )

    elif image.width == image.height and image.width > SQ_MAX_WIDTH:
        processed_image = image.resize(
            (SQ_MAX_WIDTH, SQ_MAX_WIDTH), resample=Image.Resampling.LANCZOS
        )

    else:
        return image

    return processed_image
