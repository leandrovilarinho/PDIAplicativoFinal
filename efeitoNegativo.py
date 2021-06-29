# -*- coding: utf-8 -*-
import sys
from PIL import Image

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

imgOriginal = Image.open(sys.argv[1])

# filtro NEGATIVO
matrix = imgOriginal.load()
for i in range(imgOriginal.size[0]):
  for j in range(imgOriginal.size[1]):
    r = 255 - matrix[i, j][0]
    g = 255 - matrix[i, j][1]
    b = 255 - matrix[i, j][2]

    matrix[i, j] = (r, g, b)
    imgNegativo = imgOriginal

imgNegativo.save(sys.argv[2])