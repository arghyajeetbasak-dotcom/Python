import PyPDF2
import os
merger=PyPDF2.PdfMerger()
pdf_folder="pdfs"

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        filepath = os.path.join(pdf_folder, filename)
        merger.append(filepath)

merger.write("merged_output.pdf")
merger.close()

print("PDFs merged successfully into 'merged_output.pdf'")