import getpass
import os
from pypdf import PdfReader, PdfWriter


def create_sample_pdf(pdf_path):
    """Create a minimal valid PDF file for testing purposes."""
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792) # Standard US Letter size
    with open(pdf_path, "wb") as sample_file:
        writer.write(sample_file)


def pdf_existed(folder):
    """Return True if folder contains at least one .pdf file (not subdirectory)."""
    ## any(): True if at least 1 item in an iterable is truthy and False if it is empty or all items are falsy
    return any(
        ## Both conditions must be true 
        name.lower().endswith(".pdf")
        and os.path.isfile(os.path.join(folder, name))
        ## os.listdir(): return a list of strings—the names of files or subdirectories inside folder
        for name in os.listdir(folder)
    )


def protect_pdfs(input_folder, output_folder, password):
    ## Ensure both input and output directories exist
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    ## Track processed files
    success_count = 0

    ## Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            if not os.path.isfile(input_path):
                continue

            try:
                reader = PdfReader(input_path)
                writer = PdfWriter()

                ## Copy all pages into the writer
                writer.append(reader)

                ## Encrypt the PDF with the password
                writer.encrypt(password)

                ## Write to the output folder
                with open(output_path, "wb") as output_file:
                    writer.write(output_file)

                print(f"Password added to: {filename}")
                success_count += 1
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

    if success_count == 0:
        print(f"No PDF files found in '{input_folder}'.")
    else:
        print(f"Done! Successfully encrypted {success_count} file(s) into '{output_folder}'.")


if __name__ == "__main__":
    input_dir = "input"
    output_dir = "output"

    ## Check if the input folder exists; if not, create it
    if not os.path.exists(input_dir):
        ## exist_ok=True: to skip creating the folder if it's already there instead of throwing a FileExistsError
        os.makedirs(input_dir, exist_ok=True)
        print(f"The '{input_dir}' folder has been created.")

    ## If input exists (or was just created) and has no PDF file, create a test PDF
    if not pdf_existed(input_dir):
        sample_pdf_path = os.path.join(input_dir, "Sample.pdf")
        create_sample_pdf(sample_pdf_path)
        print(f"No PDF found in '{input_dir}'. A sample PDF has been created at '{sample_pdf_path}'.")

    ## Keep asking the user to enter the password if empty
    while True:
        password = getpass.getpass("Enter PDF password: ")
        if password:
            break
        print("Password cannot be empty. Please try again.")

    protect_pdfs(input_dir, output_dir, password)
