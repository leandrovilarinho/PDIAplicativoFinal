  # -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageFilter

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")        


imgOriginal = Image.open(sys.argv[1])

#filtro SMOOTH_MORE
smoothMore = imgOriginal.filter(ImageFilter.SMOOTH_MORE)
smoothMore.save(sys.argv[2])