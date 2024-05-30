import os
import time
import argparse
from PyPDF2 import PdfMerger


def merge_pdfs(input_dir, output_parent_dir, max_files_per_merge=2, interval=60):
    while True:
        for subdir, _, _ in os.walk(input_dir):
            # Skip the root directory
            if subdir == input_dir:
                continue

            # Create output directory for merged PDFs
            output_dir = os.path.join(output_parent_dir, os.path.basename(subdir))
            os.makedirs(output_dir, exist_ok=True)

            # Initialize PdfFileMerger object
            merger = PdfMerger()

            pdf_files = [file for file in os.listdir(subdir) if file.endswith(".pdf")]

            for idx in range(0, len(pdf_files), max_files_per_merge):
                # Merge at most `max_files_per_merge` PDF files
                files_to_merge = pdf_files[idx:idx + max_files_per_merge]
                for file in files_to_merge:
                    filepath = os.path.join(subdir, file)
                    merger.append(filepath)

                # Write the merged PDF to the output directory
                output_filename = f"merged_{idx // max_files_per_merge + 1}.pdf"
                output_path = os.path.join(output_dir, output_filename)
                with open(output_path, "wb") as output_file:
                    merger.write(output_file)

                # delete the merged files
                for file in files_to_merge:
                    os.remove(os.path.join(subdir, file))

                print(f"PDF files merged successfully into '{output_filename}' in '{output_dir}'.")

                # Clear merger object for the next iteration
                merger = PdfMerger()

        time.sleep(interval)


def main():
    parser = argparse.ArgumentParser(description="Merge PDF files in a directory.")
    parser.add_argument("input_dir", type=str, help="Directory containing subdirectories with PDF files to merge.")
    parser.add_argument("output_parent_dir", type=str, help="Directory to save the merged PDF files.")
    parser.add_argument("--max_files_per_merge", type=int, default=2,
                        help="Maximum number of PDF files to merge at a time.")
    parser.add_argument("--interval", type=int, default=60, help="Interval (in seconds) between merge operations.")

    args = parser.parse_args()

    merge_pdfs(args.input_dir, args.output_parent_dir, args.max_files_per_merge, args.interval)


if __name__ == "__main__":
    main()
