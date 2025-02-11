import os
from googletrans import Translator
from PyPDF2 import *
import time as t
from reportlab.pdfgen import canvas
from PIL import Image



def upload():
    try:

        file = input("Enter the path of the file: ")

        with open(file, "rb") as pdf_file:
            reader = PdfReader(pdf_file)

            # Check if the file contains any pages (basic validation for a valid PDF)
            if len(reader.pages) > 0:
                print("The file has been loaded successfully.")
                print("=================================================")
                return file
            else:
                print("The PDF contains no pages.")
                return False
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
        return False
    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
        return False


def display_menu():
    print("-------------------Welcome to Krystova-------------------")
    print("[1] Merge PDFs" , "[2] Edit PDF" , "[3] Translate a PDF" , "[4] Image to PDF" , "[5] Exit" , sep="\n")

def merge_pdfs():
    while True:
        try:
            print("=================================================")
            no_files = int(input("Enter the number of files to merge: "))
            if no_files > 0:
                break
            else:
                print("Error, Please enter a number greater than 0")
        except Exception as e:
            print(f"{e}, Please enter a number!")
    print("=================================================")
    counter = 0
    Files = list()
    while True:
        path = upload()
        if path:
            counter += 1
            Files.append(path)

        if counter == no_files:
            print("All files has been loaded successfully")
            break
    print("=================================================")
    merger = PdfMerger(False , "Output.pdf")
    for path in Files:
        merger.append(path)

    desktop_path = [
                    os.path.join(os.path.expanduser("~") , "Desktop"),
                    os.path.join(os.path.expanduser("~") , "OneDrive" , "Desktop")
    ]

    file_path = next((path for path in desktop_path if os.path.exists(path)), None)
    if file_path is None:
        raise FileNotFoundError("Desktop is not found, Please Contact the developer")
    file_path = os.path.join(file_path , "Output.pdf")
    merger.write(file_path)
    print("All files has been merged successfully")
    print("=================================================")


def split_pdf():
    while True:
        file = upload()
        if file:
            break
    reader = PdfReader(file)
    is_cont = True
    pages = list()
    while is_cont:
        try:
            page_no = int(input("Enter the page number to split: "))
            if 0 < page_no <= len(reader.pages):
                pages.append(page_no)
            else:
                print("Error, Please enter a number greater than 0")
        except Exception as e:
            print(f"{e}, Please enter a number!")

        while True:
            c = input("Do you want to add another page ? (y/n): ").lower()
            if c == 'n':
                is_cont = False
                break
            elif c == 'y':
                break
            else:
                print("Error, Please enter a valid option!")
                t.sleep(1)
                continue

    writer = PdfWriter()
    for page_no in pages:
        writer.add_page(reader.pages[page_no - 1])

    desktop_path = [
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
    ]

    file_path = next((path for path in desktop_path if os.path.exists(path)), None)
    if file_path is None:
        raise FileNotFoundError("Desktop is not found, Please Contact the developer")
    file_path = os.path.join(file_path, "Output.pdf")
    writer.write(file_path)

def save_text_to_pdf(text, output_path):
    c = canvas.Canvas(output_path)
    c.drawString(50, 800, "Translated Text:")
    text_lines = text.split("\n")
    y = 780
    for line in text_lines:
        c.drawString(50, y, line)
        y -= 20
        if y < 20:  # Start a new page if out of space
            c.showPage()
            y = 800
    c.save()

def translate_pdf():
    while True:
        file = upload()
        if file:
            break
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + '\n'
    translator = Translator()

def images_to_pdf():
    while True:
        try:
            print("=================================================")
            no_files = int(input("Enter the number of Images to Convert: "))
            if no_files > 0:
                break
            else:
                print("Error, Please enter a number greater than 0")
        except Exception as e:
            print(f"{e}, Please enter a number!")
    print("=================================================")
    counter = 0
    image_paths = list()
    while True:
        path = input("Enter the path of the image: ")
        if path:
            counter += 1
            image_paths.append(path)

        if counter == no_files:
            print("All files has been loaded successfully")
            break
    print("=================================================")
    desktop_path = [
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
    ]

    file_path = next((path for path in desktop_path if os.path.exists(path)), None)
    if file_path is None:
        raise FileNotFoundError("Desktop is not found, Please Contact the developer")
    file_path = os.path.join(file_path, "Output.pdf")
    images = [Image.open(img).convert("RGB") for img in image_paths]
    images[0].save(file_path, save_all=True, append_images=images[1:])
    print("All files has been converted successfully")
    print("=================================================")



def run():
    is_running = True
    while is_running:
        display_menu()
        match input("Enter the number corresponding to your option: ") :
            case '1':
                merge_pdfs()
            case '2':
                split_pdf()
            case '3':
                print("Sorry this Option is under maintenance!")
                t.sleep(1)
            case '4':
                images_to_pdf()
            case '5':
                is_running = False
            case _:
                print("Error, Option not found!")
                t.sleep(1)


if __name__ == '__main__':
    run()
