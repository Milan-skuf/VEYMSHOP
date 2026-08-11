"""
Add bomber images to the product
"""
import os
import django
import shutil

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.catalog.models import Category, Product, ProductImage

# Create media directories if they don't exist
os.makedirs('media/products', exist_ok=True)
os.makedirs('media/products/gallery', exist_ok=True)

print("📁 Copying bomber images...")

# Copy images
brain_path = r"C:\Users\ИВАН\.gemini\antigravity\brain\775cfbe8-5c11-45dc-bb0b-a8e4acc04278"
images = [
    ("uploaded_image_1_1767448330751.png", "products/bomber_main.jpg"),
    ("uploaded_image_2_1767448330751.png", "products/gallery/bomber_back.jpg"),
    ("uploaded_image_3_1767448330751.png", "products/gallery/bomber_side.jpg"),
    ("uploaded_image_4_1767448330751.png", "products/gallery/bomber_detail.jpg"),
]

for src_name, dest_path in images:
    src = os.path.join(brain_path, src_name)
    dest = os.path.join('media', dest_path)
    if os.path.exists(src):
        shutil.copy2(src, dest)
        print(f"  ✓ Copied {src_name} → {dest_path}")

# Create category
category, _ = Category.objects.get_or_create(
    slug='outerwear',
    defaults={'name': 'Outerwear'}
)

# Create/Update bomber product
bomber, created = Product.objects.update_or_create(
    slug='block-bomber',
    defaults={
        'category': category,
        'name': '"BLOCK" Bomber',
        'price': 9760,
        'image': 'products/bomber_main.jpg',
        'description': '''Температурный режим до -20

Внешняя ткань: Водоотталкивающая доспо
Внутренняя: Полиэстер
Набивка: Синтепон 250гр

На модели размер "S", рост 182
"S": 165-175
"M": 175-185
"L": 185-190

Отправка в течении 3-х дней(обычно задержки до 7-ми дней)''',
        'is_active': True,
    }
)

print(f"\n{'✅ Created' if created else '📝 Updated'} bomber product")

# Delete old gallery images
ProductImage.objects.filter(product=bomber).delete()

# Add gallery images
gallery_images = [
    'products/gallery/bomber_back.jpg',
    'products/gallery/bomber_side.jpg',
    'products/gallery/bomber_detail.jpg',
]

for img_path in gallery_images:
    ProductImage.objects.create(product=bomber, image=img_path)
    print(f"  📸 Added gallery image: {img_path}")

print("\n🎉 Done! Refresh your browser to see the bomber with all 4 photos!")
