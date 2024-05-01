from tkinter import filedialog
from tkinter import Tk
from PIL import Image, ImageEnhance
import os

def resim_bastir(input_image_path, target_size_kb):
    # Resmi yükle
    image = Image.open(input_image_path)
    
    # Resmi kalitesini iyileştir
    enhancer = ImageEnhance.Sharpness(image)
    enhanced_image = enhancer.enhance(2.0)  # Örnek olarak, kaliteyi iki kat artırabilirsiniz
    
    # Sıkıştırma işlemi için geçici dosyaya kaydet
    temp_file_path = input_image_path + ".temp.jpg"
    enhanced_image.save(temp_file_path, format="JPEG", quality=85, optimize=True)
    
    # Yeni boyutu kontrol et
    new_image_size_kb = os.path.getsize(temp_file_path) / 1024
    
    # Yeni boyut hedef boyutun altındaysa, geçici dosyayı asıl dosyanın üzerine kaydet
    if new_image_size_kb <= target_size_kb:
        os.replace(temp_file_path, input_image_path)
        print(f"Resim başarıyla sıkıştırıldı. Yeni boyut: {new_image_size_kb:.2f} KB")
    else:
        print("Hata: Resim sıkıştırılamadı. Hedef boyut aşıldı.")

def select_image():
    root = Tk()
    root.withdraw()  # Ana pencereyi gizle
    file_path = filedialog.askopenfilename()  # Dosya seçme iletişim kutusunu aç
    if file_path:
        target_size_kb = 200  # Hedef dosya boyutu (KB)
        resim_bastir(file_path, target_size_kb)

select_image()
