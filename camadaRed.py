# -*- coding: utf-8 -*-
import sys
from PIL import Image

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

imgOriginal = Image.open(sys.argv[1])

# Camada Red
matrix = imgOriginal.load()

for i in range(imgOriginal.size[0]):
    for j in range(imgOriginal.size[1]):
      r = matrix[i,j][0]
      matrix[i,j] = (r,0,0)
      imgCamadaRed = imgOriginal

imgCamadaRed.save(sys.argv[2])