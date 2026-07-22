import fitz
import cv2
import numpy as np
import pytesseract
from PIL import Image
from tqdm import tqdm

# مسیر نصب Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

PDF_FILE = "9.pdf"
OUTPUT_FILE = "9.txt"

doc = fitz.open(PDF_FILE)

texts = []

for page_num in tqdm(range(len(doc)), desc="OCR"):

    page = doc.load_page(page_num)

    pix = page.get_pixmap(matrix=fitz.Matrix(4, 4))

    img = Image.frombytes(
        "RGB",
        [pix.width, pix.height],
        pix.samples
    )

    img = np.array(img)

    # خاکستری
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # افزایش کنتراست
    gray = cv2.equalizeHist(gray)

    # حذف نویز
    gray = cv2.GaussianBlur(gray, (3,3), 0)

    # سیاه سفید
    gray = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    text = pytesseract.image_to_string(
        gray,
        lang="fas",
        config="--oem 3 --psm 6"
    )

    texts.append(f"\n\n========== صفحه {page_num+1} ==========\n")
    texts.append(text)

doc.close()

with open(OUTPUT_FILE,"w",encoding="utf-8") as f:
    f.write("".join(texts))

print("Done.")