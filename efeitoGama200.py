# -*- coding: utf-8 -*-
import sys
from PIL import Image

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

imgOriginal = Image.open(sys.argv[1])

# filtro GAMA 2.00
matrix = imgOriginal.load()
gamma = 2.0
for i in range(imgOriginal.size[0]):
  for j in range(imgOriginal.size[1]):
    r = 255 - int((matrix[i, j][0]/255) ** gamma * 255)
    g = 255 - int((matrix[i, j][1]/255) ** gamma * 255)
    b = 255 - int((matrix[i, j][2]/255) ** gamma * 255)

    matrix[i, j] = (r, g, b)
    imgGama200 = imgOriginal

imgGama200.save(sys.argv[2])