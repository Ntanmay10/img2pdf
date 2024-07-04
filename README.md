Image to PDF Converter
This script converts image/images into a single PDF file using the Python fpdf library.

Requirements

    1. Python 3.x
    2. fpdf library (pip install fpdf)

Usage:

1. Clone the Repository:

   > - git clone <repository-url>
   > - cd image-to-pdf-converter

2. Run the Script:
   Execute the script by running:
   > - python image_to_pdf_converter.py
3. Menu Options:
   > - Option 1: Convert a single image to PDF.
   > - Option 2: Convert multiple images into a single PDF.
4. Input Requirements:

> - For Option 1, provide the path to the image and specify the path where the resulting PDF should be saved.
> - For Option 2, enter paths of multiple images. Type create pdf when finished adding images. Specify the path where the combined PDF should be saved.
>
> 5. Example:

        Menu:

        1. Single image to PDF
        2. Multiple images to single PDF
        3. Enter your choice (1 or 2): 2

> - Enter the paths of the images you want to add to the PDF. Type 'create pdf' to finish.

> - Enter the path of the image: path/to/image1.jpg

> - Enter the path of the image: path/to/image2.jpg

> - Enter the path of the image: create pdf

> - Enter the path to save the PDF (including the filename and .pdf extension): path/to/save/combined.pdf

> - PDF created successfully at path/to/save/combined.pdf

6. Notes:

   > -Ensure all specified image paths are correct and accessible.

   > -The resulting PDF will be created at the specified path.
