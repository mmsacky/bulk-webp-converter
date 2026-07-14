# Bulk WebP Converter

A fast, local batch image converter that resizes, renames, and converts large image collections into optimized WebP files for the web.

## Features

- Batch converts JPG, PNG, and GIF images to WebP
- Automatically resizes images while preserving their aspect ratio
- Handles landscape, portrait, and square images intelligently
- Choose from built-in quality presets:
  - Low
  - Medium
  - High
  - Lossless
- Or specify a custom quality level (1–100)
- Optional batch renaming with automatic sequential numbering

## Requirements

- Python 3.10 or later

## Installation

### End Users (Recommended)

Install `pipx` if you don't already have it:

```bash
brew install pipx
pipx ensurepath
```

Then install the application globally:

```bash
pipx install .
```

### Development

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/mmsacky/bulk-webp-converter.git
cd bulk-webp-converter
pip install -e .
```

## Usage

Launch the application from any terminal:

```bash
bulk-webp-converter
```

Alternatively:

```bash
python -m bulk_webp_converter
```

The application will guide you through the following steps:

1. Enter the absolute path to the folder containing your source images.
   Example:

   ```
   /Users/username/Downloads/test-images
   ```

2. Select an output quality:
   - Low
   - Medium
   - High
   - Lossless
   - Custom (1–100)

3. Choose whether to rename the converted images.
   - If enabled, enter a base filename (for example, `product_image`).
   - Files will automatically be named:
     ```
     product_image_01.webp
     product_image_02.webp
     product_image_03.webp
     ```

4. The converter processes every supported image in the folder and saves the results to:

   ```
   Converted-Images/
   ```

   inside the original source folder.

## License

Released under the MIT License.