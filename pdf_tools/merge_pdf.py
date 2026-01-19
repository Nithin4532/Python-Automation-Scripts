from PyPDF2 import PdfMerger

merger = PdfMerger()

pdfs = ["file1.pdf", "file2.pdf"]

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()

print("PDFs merged successfully!")
