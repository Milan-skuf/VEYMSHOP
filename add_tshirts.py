"""
Script to add T-shirt category and products to the database.
Run with: python add_tshirts.py
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.catalog.models import Category, Product

def add_tshirts():
    # Create T-shirts category
    category, created = Category.objects.get_or_create(
        slug='tshirts',
        defaults={'name': 'T-Shirts'}
    )
    
    if created:
        print(f"✅ Created category: {category.name}")
    else:
        print(f"ℹ️  Category already exists: {category.name}")
    
    # T-shirt products data
    tshirts = [
        {
            'name': 'RED "NOMAD" TEE',
            'slug': 'red-nomad-tee',
            'price': 1490,
            'description': """Premium cotton t-shirt with unique design.
            
Fabric density: 190gr/m2
100% cotton
Overlock seams construction

Model wears size L (height 182cm)

Shipping within 7 days (usually faster 1-3 days)""",
            'image': 'products/red_tshirt.png',
        },
        {
            'name': 'CLASSIC BLACK TEE',
            'slug': 'classic-black-tee',
            'price': 1490,
            'description': """Essential black t-shirt for any wardrobe.
            
Fabric density: 190gr/m2
100% premium cotton
Reinforced collar
Overlock seams

Perfect fit for everyday wear.
Shipping within 7 days.""",
            'image': 'products/black_tshirt.png',
        },
        {
            'name': 'MINIMAL WHITE TEE',
            'slug': 'minimal-white-tee',
            'price': 1490,
            'description': """Clean white t-shirt with minimalist aesthetic.
            
Fabric density: 190gr/m2
100% premium cotton
Soft touch fabric
Reinforced seams

Timeless piece for your collection.
Shipping within 7 days.""",
            'image': 'products/white_tshirt.png',
        },
    ]
    
    # Add products
    for tshirt_data in tshirts:
        product, created = Product.objects.get_or_create(
            slug=tshirt_data['slug'],
            defaults={
                'category': category,
                'name': tshirt_data['name'],
                'price': tshirt_data['price'],
                'description': tshirt_data['description'],
                'image': tshirt_data['image'],
                'is_active': True,
            }
        )
        
        if created:
            print(f"✅ Created product: {product.name}")
        else:
            print(f"ℹ️  Product already exists: {product.name}")
    
    print("\n🎉 Done! T-shirts have been added to the database.")
    print(f"📊 Total products in T-Shirts category: {category.products.count()}")

if __name__ == '__main__':
    try:
        add_tshirts()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n⚠️  Make sure you've run migrations first:")
        print("   python manage.py makemigrations")
        print("   python manage.py migrate")
