import getpass
import os
from pypdf import PdfReader, PdfWriter


def create_sample_pdf(pdf_path):
    """Create a minimal valid PDF file for testing purposes."""
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)  # Standard US Letter size
    with open(pdf_path, "wb") as sample_file:
        writer.write(sample_file)


def has_pdf_files(folder):
    """Return True if folder contains at least one .pdf file (not subdirectory)."""
    return any(
        entry.lower().endswith(".pdf")
        and os.path.isfile(os.path.join(folder, entry))
        for entry in os.listdir(folder)
    )


def protect_pdfs(input_folder, output_folder, password):
    # Ensure both input and output directories exist
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    # Track processed files count
    success_count = 0

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            if not os.path.isfile(input_path):
                continue

            try:
                reader = PdfReader(input_path)
                writer = PdfWriter()

                # Copy all pages into the writer
                writer.append(reader)

                # Encrypt the PDF with the password
                writer.encrypt(password)

                # Write to the output folder
                with open(output_path, "wb") as output_file:
                    writer.write(output_file)

                print(f"Protected: {filename}")
                success_count += 1
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

    if success_count == 0:
        print(f"No PDF files found in '{input_folder}'.")
    else:
        print(
            f"\nDone! Successfully encrypted {success_count} file(s) into '{output_folder}'."
        )


if __name__ == "__main__":
    # Configuration
    INPUT_DIR = "input"
    OUTPUT_DIR = "output"

    # 1. Check if the input folder exists; if not, create it
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR, exist_ok=True)
        print(f"Created missing '{INPUT_DIR}' folder.")
    elif not os.path.isdir(INPUT_DIR):
        raise NotADirectoryError(f"'{INPUT_DIR}' exists and is not a directory.")

    # 2. If input exists (or was just created) and has no PDF file, create a test PDF
    if not has_pdf_files(INPUT_DIR):
        sample_pdf_path = os.path.join(INPUT_DIR, "sample_test.pdf")
        create_sample_pdf(sample_pdf_path)
        print(f"No PDF found in '{INPUT_DIR}'. Created test PDF at '{sample_pdf_path}'.")

    while True:
        password = getpass.getpass("Enter PDF password: ")
        if password:
            break
        print("Password cannot be empty. Please try again.")

    protect_pdfs(INPUT_DIR, OUTPUT_DIR, password)