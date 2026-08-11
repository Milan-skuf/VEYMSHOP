"""
Script to add Bomber jacket to the database.
Run with: python add_bomber.py
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.catalog.models import Category, Product, ProductImage

def add_bomber():
    # Create Outerwear category
    category, created = Category.objects.get_or_create(
        slug='outerwear',
        defaults={'name': 'Outerwear'}
    )
    
    if created:
        print(f"✅ Created category: {category.name}")
    else:
        print(f"ℹ️  Category already exists: {category.name}")
    
    # Bomber product data
    bomber_data = {
        'name': '"BLOCK" Bomber',
        'slug': 'block-bomber',
        'price': 9760,
        'description': """Temperature rating up to -20°C

Outer fabric: Water-repellent fabric
Inner lining: Polyester
Filling: Sintepon 250g

Model wears size S (height 182cm)
S: 165-175cm
M: 175-185cm  
L: 185-190cm

Shipping within 3-4 days (usually faster; delays up to 7 days)""",
        'image': 'products/bomber/bomber_main.jpg',
    }
    
    # Add bomber
    product, created = Product.objects.get_or_create(
        slug=bomber_data['slug'],
        defaults={
            'category': category,
            'name': bomber_data['name'],
            'price': bomber_data['price'],
            'description': bomber_data['description'],
            'image': bomber_data['image'],
            'is_active': True,
        }
    )
    
    if created:
        print(f"✅ Created product: {product.name}")
        
        # Add additional product images
        gallery_images = [
            'products/bomber/bomber_back.jpg',
            'products/bomber/bomber_side.jpg',
            'products/bomber/bomber_detail.jpg',
        ]
        
        for img_path in gallery_images:
            ProductImage.objects.create(
                product=product,
                image=img_path
            )
            print(f"  📸 Added gallery image: {img_path}")
    else:
        print(f"ℹ️  Product already exists: {product.name}")
    
    print("\n🎉 Done! Bomber has been added to the database.")
    print(f"📊 Total products in Outerwear category: {category.products.count()}")

if __name__ == '__main__':
    try:
        add_bomber()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n⚠️  Make sure you've run migrations first:")
        print("   python manage.py makemigrations")
        print("   python manage.py migrate")
