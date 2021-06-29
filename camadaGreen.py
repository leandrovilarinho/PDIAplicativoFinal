# -*- coding: utf-8 -*-
import sys
from PIL import Image

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

imgOriginal = Image.open(sys.argv[1])

# Camada Green
matrix = imgOriginal.load()

for i in range(imgOriginal.size[0]):
    for j in range(imgOriginal.size[1]):
      g = matrix[i,j][1]
      matrix[i,j] = (0,g,0)
      imgCamadaGreen = imgOriginal

imgCamadaGreen.save(sys.argv[2])