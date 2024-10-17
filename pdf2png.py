import PyPDF2
import os
#from PIL import Image

def pdf2images(pdf_path):
    script_dir = os.path.dirname(__file__)
    script_dir = os.path.join(script_dir, "img_output")

    if not os.path.exists(script_dir):
        os.mkdir(script_dir)
    else:
        for f in os.listdir(script_dir):
            os.remove(os.path.join(script_dir,f))
        os.rmdir(script_dir)
        os.mkdir(script_dir)


    file = open(pdf_path, 'rb')
    reader = PyPDF2.PdfReader(file)
   
    for p in range(len(reader.pages)):
        page = reader.pages[p]
        print(f"El nuevo:\n{page.get_contents}")
        print(f"Para la página {p+1} las dimensiones de la imagen son: \nAltura: {int(page.mediabox.height)}\tAnchura: {page.mediabox.width}")
        image_per_page_c = 0
        for image_f in page.images:
           image_save = f"{p}{image_per_page_c}{image_f.name}"
           image_path = os.path.join(script_dir, image_save)
           print(f"Escribiendo {image_path}...")
           with open(image_path, "wb") as fp:
               fp.write(image_f.data)
               image_per_page_c += 1