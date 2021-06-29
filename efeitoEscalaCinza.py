# -*- coding: utf-8 -*-
import sys
from PIL import Image

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

imgOriginal = Image.open(sys.argv[1])

# filtro Escala de Cinza
matrix = imgOriginal.load()

for i in range(imgOriginal.size[0]):
    for j in range(imgOriginal.size[1]):
      r = matrix[i,j][0]
      g = matrix[i,j][1]
      b = matrix[i,j][2]
      pixel = int((r + g + b)/3) 
      matrix[i,j] = (pixel, pixel, pixel)
      imgEscalaCinza = imgOriginal

imgEscalaCinza.save(sys.argv[2])