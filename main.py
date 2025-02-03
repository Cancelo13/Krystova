from PyPDF2 import *
import time as t

def upload():
    try:
        file = input("Enter the file name: ")

        # Open the file and create a PdfReader instance
        with open(file, "rb") as pdf_file:
            reader = PdfReader(pdf_file)

            # Check if the file contains any pages (basic validation for a valid PDF)
            if len(reader.pages) > 0:
                print("The PDF is valid and has been loaded successfully.")
                return True
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



def run():
    is_running = True
    while is_running:
        display_menu()
        option = input("Enter the number corresponding to your option: ")
        if option == '5':
            is_running = False
        elif option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        else:
            print("Error, Option not found!")
            t.sleep(1)




if __name__ == '__main__':
    run()
