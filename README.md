
# PDFtoJPG

A Python tool to convert PDF documents into JPG images using the `pdf2image` library.

## Description

PDFtoJPG leverages the `pdf2image` Python library, which is a wrapper around the Poppler utilities (`pdftoppm` and `pdftocairo`), to convert each page of a PDF file into high-quality JPG images. This is useful for extracting images from PDFs, preparing documents for OCR, or simply converting PDFs into a more accessible image format.

## Features

- Convert each page of a PDF into a separate JPG image.
- Supports high-resolution output with configurable DPI.
- Easy to use with minimal setup.
- Cross-platform (Windows, macOS, Linux) with Poppler installed.

## Requirements

- Python 3.x
- [pdf2image](https://pypi.org/project/pdf2image/)
- Poppler utilities installed on your system

### Installing Poppler

- **Windows:** Download from [poppler for Windows](http://blog.alivate.com.au/poppler-windows/) and add the `bin` folder to your PATH.
- **macOS:** Install via Homebrew:
  ```
  brew install poppler
  ```
- **Linux:** Install via your package manager, e.g.:
  ```
  sudo apt-get install poppler-utils
  ```

## Installation

Install the Python dependencies:

```
pip install pdf2image Pillow
```

## Usage

Basic example to convert a PDF into JPG images:

```
from pdf2image import convert_from_path

# Path to your PDF file
pdf_path = 'example.pdf'

# Convert PDF pages to images
pages = convert_from_path(pdf_path, dpi=300)

# Save each page as a JPG file
for i, page in enumerate(pages, start=1):
    page.save(f'page_{i}.jpg', 'JPEG')
```

### Notes

- You may need to specify the `poppler_path` argument in `convert_from_path` if Poppler is not in your system PATH (especially on Windows):

```
pages = convert_from_path(pdf_path, dpi=300, poppler_path=r'C:\path\to\poppler\bin')
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

