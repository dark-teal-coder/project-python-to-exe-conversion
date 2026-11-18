import os
from pypdf import PdfReader, PdfWriter


def protect_pdfs(input_folder, output_folder, password):
  # Ensure the output directory exists
  os.makedirs(output_folder, exist_ok=True)

  # Check if the input folder exists
  if not os.path.exists(input_folder):
    print(f"Error: The input folder '{input_folder}' does not exist.")
    return

  # Track processed files count
  success_count = 0

  # Iterate through all files in the input folder
  for filename in os.listdir(input_folder):
    if filename.lower().endswith(".pdf"):
      input_path = os.path.join(input_folder, filename)
      output_path = os.path.join(output_folder, filename)

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

  print(
      f"\nDone! Successfully encrypted {success_count} file(s) into '{output_folder}'."
  )


if __name__ == "__main__":
  # Configuration
  INPUT_DIR = "input"
  OUTPUT_DIR = "output"
  PASSWORD = (  # Change this to your desired password
      "YourSecurePassword123"
  )

  protect_pdfs(INPUT_DIR, OUTPUT_DIR, PASSWORD)
