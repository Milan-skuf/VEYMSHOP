"""
Add Sweatpants "NOMAD" product with all gallery images
Run: python add_sweatpants.py
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

print("📁 Copying sweatpants images...")

# Copy images
brain_path = r"C:\Users\ИВАН\.gemini\antigravity\brain\775cfbe8-5c11-45dc-bb0b-a8e4acc04278"
images = [
    ("uploaded_image_1_1767450095445.png", "products/sweatpants_main.jpg"),
    ("uploaded_image_2_1767450095445.png", "products/gallery/sweatpants_front.jpg"),
    ("uploaded_image_3_1767450095445.png", "products/gallery/sweatpants_chart.jpg"),
]

for src_name, dest_path in images:
    src = os.path.join(brain_path, src_name)
    dest = os.path.join('media', dest_path)
    if os.path.exists(src):
        shutil.copy2(src, dest)
        print(f"  ✓ {src_name} → {dest_path}")

# Get or create Bottoms category
category, _ = Category.objects.get_or_create(
    slug='bottoms',
    defaults={'name': 'Bottoms'}
)

# Create Sweatpants
sweatpants, created = Product.objects.update_or_create(
    slug='nomad-sweatpants',
    defaults={
        'category': category,
        'name': 'Sweatpants "NOMAD"',
        'price': 3860,
        'image': 'products/sweatpants_main.jpg',
        'description': '''плотность - 450гр/м2
100% хлопок
футер 3-х нитка
скрытые шнурки

На фото «Никита» его рост 182 он носит размер «1»

Отправка до 7 дней(обычно каждые 3 дня)''',
        'is_active': True,
    }
)

print(f"\n{'✅ Created' if created else '📝 Updated'} Sweatpants")

# Delete old gallery images
ProductImage.objects.filter(product=sweatpants).delete()

# Add gallery images
gallery_images = [
    'products/gallery/sweatpants_front.jpg',
    'products/gallery/sweatpants_chart.jpg',
]

for img_path in gallery_images:
    ProductImage.objects.create(product=sweatpants, image=img_path)
    print(f"  📸 Added: {img_path}")

print("\n🎉 Done! Sweatpants added with all photos!")
print("   Refresh http://127.0.0.1:8000/ to see it!")
