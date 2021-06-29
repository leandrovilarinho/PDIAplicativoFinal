 # -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageFilter

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")        


imgOriginal = Image.open(sys.argv[1])

#filtro 2 KERNEL
kernel2 = ImageFilter.Kernel((3,3), (0,1,0,1,-4,1,0,1,0), 1, 0)
kernelB = imgOriginal.filter(kernel2)
kernelB.save(sys.argv[2])