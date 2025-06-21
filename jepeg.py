import os
from pdf2image import convert_from_path

def pdf_to_jpg(pdf_path, output_folder, dpi=300, poppler_path=None):
    """
    Convert all pages of a PDF to JPG images.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_folder (str): Folder to save the JPG images.
        dpi (int): Resolution of the output images.
        poppler_path (str or None): Path to the Poppler bin folder (required on Windows).
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF to images
    images = convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)

    # Save each page as a JPG file
    for i, image in enumerate(images, start=1):
        output_path = os.path.join(output_folder, f"page_{i}.jpg")
        image.save(output_path, "JPEG")
        print(f"Saved {output_path}")

if __name__ == "__main__":
    # Example usage:
    # Replace these paths with your actual PDF file and desired output folder
    pdf_file = "example.pdf"
    output_dir = "output_images"

    # On Windows, specify the path to the Poppler bin folder, e.g.:
    # poppler_bin_path = r"C:\path\to\poppler\bin"
    # On macOS/Linux, set to None if Poppler is in your PATH
    poppler_bin_path = None

    pdf_to_jpg(pdf_file, output_dir, dpi=300, poppler_path=poppler_bin_path)
