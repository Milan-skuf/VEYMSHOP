"""
Script to rename categories and assign products correctly.
Run: python update_categories.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.catalog.models import Category, Product

def update_categories():
    # Desired Categories
    category_map = {
        't-shirts': 'ФУТБОЛКА',
        'outerwear': 'БОМБЕР',
        'bottoms': 'ШТАНЫ'
    }

    for slug, name in category_map.items():
        cat, created = Category.objects.get_or_create(slug=slug)
        cat.name = name
        cat.save()
        print(f"{'✅ Created' if created else '📝 Updated'} category: {name} ({slug})")

    # Double check assignments (optional, but good for verification)
    print("\nProduct assignments:")
    for p in Product.objects.all():
        print(f"  - {p.name}: {p.category.name if p.category else 'No Category'}")

if __name__ == '__main__':
    update_categories()
