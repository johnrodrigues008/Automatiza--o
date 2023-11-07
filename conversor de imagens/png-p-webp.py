from PIL import Image
import os

def convert_images_in_folder(input_folder, output_folder, output_format):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + "." + output_format)

        if filename.endswith(".png"):
            img = Image.open(input_path)
            img.save(output_path, output_format)

if __name__ == "__main__":
    input_folder = r'C:/Users\johnr\OneDrive\Área de Trabalho\Angular\exemplo\src\assets\icons'  # Substitua pelo diretório das imagens
    output_folder = r'C:\Users\johnr\OneDrive\Área de Trabalho\Angular\exemplo\src\assets\icons'   # Substitua pelo diretório de saída
    output_format = "webp"  # Formato de saída, você pode alterá-lo para outros formatos

    convert_images_in_folder(input_folder, output_folder, output_format)
import os
