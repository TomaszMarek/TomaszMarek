import sys
import os
import cv2
import numpy as np
from PIL import Image
from rembg import remove


def prep_photo(input_path: str, output_path: str = "source-prepped.png"):
    if not os.path.exists(input_path):
        print(f"Błąd: Nie znaleziono pliku {input_path}")
        sys.exit(1)

    print("Krok 1/3: Usuwanie tła...")
    input_image = Image.open(input_path)
    no_bg = remove(input_image)

    rgba = np.array(no_bg)

    print("Krok 2/3: Nakładanie na białe tło i odcienie szarości...")
    alpha = rgba[:, :, 3] / 255.0
    rgb = rgba[:, :, :3]

    white_bg = np.ones_like(rgb, dtype=np.uint8) * 255
    blended = (rgb * alpha[:, :, None] + white_bg * (1 - alpha[:, :, None])).astype(np.uint8)
    gray = cv2.cvtColor(blended, cv2.COLOR_RGB2GRAY)

    print("Krok 3/3: Wyrównywanie kontrastu (CLAHE)...")
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    cv2.imwrite(output_path, enhanced)
    print(f"Sukces! Przygotowany obraz zapisano jako: {output_path}")


if __name__ == "__main__":
    photo_file = sys.argv[1] if len(sys.argv) > 1 else "source-photo.jpg"
    prep_photo(photo_file)