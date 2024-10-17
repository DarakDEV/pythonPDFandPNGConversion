import os
import png2pdf as toPdf
import pdf2png as toPng
if __name__ == "__main__":
    print("Iniciando script....")
    script_dir = os.path.dirname(__file__)
    IMG_DIRECTORY = os.path.join(script_dir, "images")
    PDF_DIRECTORY = os.path.join(script_dir,"resultado.pdf")
    print(PDF_DIRECTORY)
    toPdf.images2pdf(IMG_DIRECTORY, PDF_DIRECTORY)
    print("Finalizada la conversión de imágenes a PDF")
    print(f"\n\nIniciando conversión de pdf a imágenes {PDF_DIRECTORY}...")
    toPng.pdf2images(PDF_DIRECTORY)
    print("\nFinalizando Script...")