 # -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageFilter

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")        


imgOriginal = Image.open(sys.argv[1])

#filtro 3 KERNEL
kernel3 = ImageFilter.Kernel((3,3), (-1,-1,-1,-1,8,-1,-1,-1,-1), 1, 0)
kernelC = imgOriginal.filter(kernel3)
kernelC.save(sys.argv[2])