import os
import sys
from pdf2image import convert_from_path


def pdf_to_images(pdf_path):
    # Get the base name of the PDF (without extension)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_dir = os.path.join(os.path.dirname(pdf_path), base_name)
    os.makedirs(output_dir, exist_ok=True)

    # Convert PDF to images
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images, start=1):
        image_path = os.path.join(output_dir, f"{i}.png")
        image.save(image_path, 'PNG')
        print(f"Saved: {image_path}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_image.py <path_to_pdf>")
        sys.exit(1)
    pdf_path = sys.argv[1]
    if not os.path.isfile(pdf_path):
        print(f"File not found: {pdf_path}")
        sys.exit(1)
    pdf_to_images(pdf_path)


if __name__ == "__main__":
    main() 