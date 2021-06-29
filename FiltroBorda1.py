  # -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageFilter

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")        


imgOriginal = Image.open(sys.argv[1])

#filtro 1 KERNEL
kernel = ImageFilter.Kernel((3,3), (1,0,-1,0,0,0,-1,0,1), 1, 0)
kernelA = imgOriginal.filter(kernel)
kernelA.save(sys.argv[2])