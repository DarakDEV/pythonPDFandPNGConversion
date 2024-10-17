import os
from PIL import Image

def images2pdf(images_path, pdf_path):
    png_files = [os.path.join(images_path,file) for file in os.listdir(images_path) if file.endswith('.png')]
    print(f"Las imágenes son: {png_files}")
    images = [Image.open(f) for f in png_files]
    pdfGen(images,pdf_path)

def pdfGen(image_list, pdf_path):
    image_list[0].save(pdf_path, "PDF", resolution = 100.0, save_all = True, append_images = image_list[1:])