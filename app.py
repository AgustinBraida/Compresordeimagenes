# Libreria para comprimir imagenes
from PIL import Image 
# Libreria que nos permite leer los archivos
import os


# Definimos la carpeta en donde estan los archivos
descargaArchivos = '/Users/agust/OneDrive/Imágenes del celular/Camara Compu/'

if __name__ == '__main__':
    for nombre in os.listdir(descargaArchivos):
        name, extension = os.path.splitext(descargaArchivos + nombre)

        # filtramos por la extención
        if extension in ['.jpg', '.jpeg', '.png']:
            imagen = Image.open(descargaArchivos + nombre)
            imagen.save(descargaArchivos + 'Comprimido_' + nombre, optimize=True, quality=60)

