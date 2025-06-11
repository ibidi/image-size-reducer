# 🖼️ Görsel Boyut Küçültücü (JPEG & PNG)

Python ile yazılmış bu script, `.jpg`, `.jpeg`, `.png` uzantılı görselleri optimize ederek boyutlarını küçültür. Ayrıca EXIF verilerini okuyarak görüntüleri doğru yönde tutar.

## 🚀 Özellikler

- JPEG görsellerde kalite düşürerek sıkıştırma
- PNG görsellerde optimize etme
- EXIF yön bilgisine göre görseli otomatik düzeltme
- Toplu görsel işleme desteği

## 📂 Klasör Yapısı

gorsel_sikistirici/
├── main.py
├── resimler/
│ ├── ornek1.jpg
│ └── ornek2.png
└── sikistirilmis/


## ⚙️ Kurulum

```bash
pip install pillow
```
## ▶️ Kullanım

resimler/ klasörüne görsellerinizi atın.
main.py dosyasını çalıştırın:
```bash
python main.py
```
Sıkıştırılmış görseller sikistirilmis/ klasörüne kaydedilecektir.

## ⚠️ Uyarı
Bu script sadece yerel ve yasal kullanım için tasarlanmıştır.
Orijinal dosyalar silinmez, kopyalanarak optimize edilir.
