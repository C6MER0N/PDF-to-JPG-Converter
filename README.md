# PDF to JPEG Converter
This Python program provides a simple graphical user interface (GUI) to convert a PDF file into JPEG images, one per page. It uses the tkinter library for the GUI and pdf2image for converting PDF pages to images.

## Features
- Select PDF: Choose a PDF file to convert.
- Select Output Folder: Choose the folder where the JPEG images will be saved.
- Convert: Convert the PDF pages into JPEG images.
- Poppler Requirement: The program relies on Poppler utilities for PDF rendering, which needs to be installed.


## Requirements
- Python 3.x
- Tkinter (for GUI)
- pdf2image (for PDF to image conversion)
- Poppler (PDF rendering library)

To install the necessary Python packages, use:
```pip install pdf2image ```
        
Poppler Installation
Windows: Download Poppler from [here](https://github.com/oschwartz10612/poppler-windows/releases/tag/v24.08.0-0), and extract the contents. Set the poppler_path in the script to the location of the Poppler bin folder.

Mac: You can install Poppler using Homebrew:
      ``` brew install poppler```

Linux: Install Poppler using your package manager. For example, on Ubuntu:
      ``` sudo apt-get install poppler-utils```

# Usage 
- **Select PDF**: Choose a PDF file to convert.
- **Select Output**: Folder: Click this button to choose the folder where the JPEG images will be saved.
- **Convert**: Click this button to start the conversion.
- **Poppler Path**: Ensure that the path to your Poppler installation is correctly set in the ```poppler_path``` variable in the code.

# Example
Once the PDF and output folder are selected, click "Convert" to start the conversion process. Each page of the PDF will be saved as a JPEG image in the selected folder. The file names will follow the format ```pdfname_page_X.jpg```

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
