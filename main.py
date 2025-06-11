from PIL import Image, ExifTags
import os

def exif_dondur(img):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = img._getexif()
        if exif is not None:
            yon = exif.get(orientation)
            if yon == 3:
                img = img.rotate(180, expand=True)
            elif yon == 6:
                img = img.rotate(270, expand=True)
            elif yon == 8:
                img = img.rotate(90, expand=True)
    except:
        pass
    return img

def resim_kucult(dosya_yolu, hedef_klasor, kalite=70):
    if not os.path.exists(hedef_klasor):
        os.makedirs(hedef_klasor)

    for dosya in os.listdir(dosya_yolu):
        if dosya.lower().endswith(('.png', '.jpg', '.jpeg')):
            tam_yol = os.path.join(dosya_yolu, dosya)
            img = Image.open(tam_yol)
            img = exif_dondur(img)  # EXIF rotasını düzelt

            hedef_yol = os.path.join(hedef_klasor, dosya)

            if dosya.lower().endswith('.png'):
                img.save(hedef_yol, optimize=True)
            else:
                img.save(hedef_yol, quality=kalite, optimize=True)

            print(f"[✓] Sıkıştırıldı ve düzeltildi: {dosya}")

# Kullanım
kaynak_klasor = "resimler"
hedef_klasor = "sikistirilmis"

resim_kucult(kaynak_klasor, hedef_klasor)
