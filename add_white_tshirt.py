"""
Add White T-shirt product with all gallery images
Run: python add_white_tshirt.py
"""
import os
import django
import shutil

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.catalog.models import Category, Product, ProductImage

# Create media directories
os.makedirs('media/products', exist_ok=True)
os.makedirs('media/products/gallery', exist_ok=True)

print("📁 Copying white T-shirt images...")

# Copy images
brain_path = r"C:\Users\ИВАН\.gemini\antigravity\brain\775cfbe8-5c11-45dc-bb0b-a8e4acc04278"
images = [
    ("uploaded_image_0_1767449893544.png", "products/white_tshirt_main.jpg"),
    ("uploaded_image_1_1767449893544.png", "products/gallery/white_tshirt_2.jpg"),
    ("uploaded_image_2_1767449893544.png", "products/gallery/white_tshirt_chart.jpg"),
]

for src_name, dest_path in images:
    src = os.path.join(brain_path, src_name)
    dest = os.path.join('media', dest_path)
    if os.path.exists(src):
        shutil.copy2(src, dest)
        print(f"  ✓ {src_name} → {dest_path}")

# Get T-Shirts category
category, _ = Category.objects.get_or_create(
    slug='t-shirts',
    defaults={'name': 'T-Shirts'}
)

# Create White T-shirt
white_tshirt, created = Product.objects.update_or_create(
    slug='white-tshirt',
    defaults={
        'category': category,
        'name': 'White',
        'price': 990,
        'image': 'products/white_tshirt_main.jpg',
        'description': '''плотность - 180гр/м2
100% хлопок
оверлок швы

На фото «Никита» его рост 182 он носит размер «XS»

Отправка в течении 7 дней (обычно быстрее 1-3 дня)''',
        'is_active': True,
    }
)

print(f"\n{'✅ Created' if created else '📝 Updated'} White T-shirt")

# Delete old gallery images
ProductImage.objects.filter(product=white_tshirt).delete()

# Add gallery images
gallery_images = [
    'products/gallery/white_tshirt_2.jpg',
    'products/gallery/white_tshirt_chart.jpg',
]

for img_path in gallery_images:
    ProductImage.objects.create(product=white_tshirt, image=img_path)
    print(f"  📸 Added: {img_path}")

print("\n🎉 Done! White T-shirt added with all photos!")
print("   Refresh http://127.0.0.1:8000/ to see it!")
