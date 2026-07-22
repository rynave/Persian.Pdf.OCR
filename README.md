# 📄 Persian PDF OCR

استخراج متن فارسی از فایل‌های PDF با استفاده از **PyMuPDF + OpenCV + Tesseract OCR**.

این پروژه صفحات PDF را با کیفیت بالا رندر می‌کند، تصویر را پیش‌پردازش می‌کند و سپس با استفاده از Tesseract متن فارسی را استخراج کرده و در یک فایل متنی ذخیره می‌کند.

---

## ✨ ویژگی‌ها

- استخراج متن از PDF
- پشتیبانی از زبان فارسی
- افزایش کیفیت OCR با پیش‌پردازش تصویر
- نمایش نوار پیشرفت (Progress Bar)
- ذخیره خروجی در فایل `.txt`

---

## 📦 کتابخانه‌های مورد نیاز

```bash
pip install pymupdf opencv-python numpy pillow pytesseract tqdm
```

---

## 🔧 نصب Tesseract OCR

ابتدا Tesseract OCR را نصب کنید.

دانلود:

https://github.com/UB-Mannheim/tesseract/wiki

پس از نصب، مسیر آن را در کد تنظیم کنید:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

اگر مسیر نصب شما متفاوت است، آن را تغییر دهید.

---

## 📁 ساختار پروژه

```
project/
│
├── app.py
├── 9.pdf
└── 9.txt
```

---

## ▶️ نحوه اجرا

فایل PDF ورودی را مشخص کنید:

```python
PDF_FILE = "9.pdf"
```

نام فایل خروجی را تعیین کنید:

```python
OUTPUT_FILE = "9.txt"
```

سپس اجرا کنید:

```bash
python app.py
```

---

## ⚙️ مراحل پردازش

برای هر صفحه:

1. تبدیل صفحه PDF به تصویر با رزولوشن بالا
2. تبدیل تصویر به خاکستری
3. افزایش کنتراست
4. حذف نویز
5. تبدیل به تصویر سیاه و سفید (Otsu Threshold)
6. استخراج متن با Tesseract OCR
7. ذخیره متن در فایل خروجی

---

## 📚 کتابخانه‌های استفاده شده

- PyMuPDF
- OpenCV
- NumPy
- Pillow
- pytesseract
- tqdm

---

## 📌 نکات

- برای بهترین نتیجه از PDFهای با کیفیت استفاده کنید.
- مدل زبان فارسی (`fas.traineddata`) باید در پوشه `tessdata` نصب شده باشد.
- در صورت نیاز می‌توانید تنظیمات `--psm` و `--oem` را برای دقت بیشتر تغییر دهید.

---

## 📄 نمونه خروجی

```
========== صفحه 1 ==========
متن استخراج شده...

========== صفحه 2 ==========
متن استخراج شده...
```

---

## 🤝 مشارکت

اگر پیشنهادی برای بهبود دقت OCR یا افزایش امکانات پروژه دارید، خوشحال می‌شوم Pull Request یا Issue ثبت کنید.

---

## 📜 License

This project is licensed under the MIT License.