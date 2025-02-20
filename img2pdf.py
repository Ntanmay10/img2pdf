from fpdf import FPDF
import os
import platform

def clear_screen():
    # Clear screen based on the operating system
    if platform.system() == 'Windows':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux and macOS

def image_to_pdf(image_paths, pdf_path):
    
    pdf = FPDF(unit='pt')  # Create instance of FPDF class (unit in points)

    for image_path in image_paths:
        pdf.add_page()  # Add a new page to the PDF
        
        # Get image dimensions
        pdf.image(image_path, x=0, y=0, w=260, h=297)  # Insert image into PDF, size A4
        img_width = pdf.w
        img_height = pdf.h
        
        # Calculate center coordinates
        x_pos = (pdf.w - img_width) / 2
        y_pos = (pdf.h - img_height) / 2
        
        pdf.image(image_path, x=x_pos, y=y_pos, w=img_width, h=img_height)  # Centered image
        
    pdf.output(pdf_path)  # Output PDF to specified path
    print(f"PDF created successfully at {pdf_path}")

def main():
    """
    Main function to handle user input and program flow.
    """
    clear_screen()
    
    print("********************************************")
    print("*                                          *")
    print("*              Image to PDF                *")
    print("*                                          *")
    print("********************************************")
    print("\nMenu:")
    print("1. Single image to PDF")
    print("2. Multiple images to single PDF")
    
    choice = input("\nEnter your choice (1 or 2): ")  # Prompt user for choice
    
    if choice == '1':  # Convert single image to PDF
        image_path = input("Enter the path of the image: ")
        if os.path.isfile(image_path):  # Check if file exists at given path
            pdf_path = input("Enter the path to save the PDF (including the filename and .pdf extension): ")
            image_to_pdf([image_path], pdf_path)  # Call function to convert single image to PDF
        else:
            print("Invalid file path. Please try again.")
    elif choice == '2':  # Convert multiple images to single PDF
        image_paths = []
        print("Enter the paths of the images you want to add to the PDF. Type 'create pdf' to finish.")
        while True:
            image_path = input("Enter the path of the image: ")
            if image_path.lower() == 'create pdf':  # Check if user wants to finish adding images
                break
            if os.path.isfile(image_path):  # Check if file exists at given path
                image_paths.append(image_path)  # Add valid image path to list
            else:
                print("Invalid file path. Please try again.")
        
        if image_paths:
            pdf_path = input("Enter the path to save the PDF (including the filename and .pdf extension): ")
            image_to_pdf(image_paths, pdf_path)  # Call function to convert multiple images to PDF
        else:
            print("No images provided.")
    else:
        print("Invalid choice. Please run the program again and select a valid option.")

if __name__ == '__main__':
    main()
