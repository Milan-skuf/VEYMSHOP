"""
Quick script to add the Bomber jacket product
Run: python quick_add_bomber.py
"""
import os
import django
import shutil

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.catalog.models import Category, Product

# Create category
category, _ = Category.objects.get_or_create(
    slug='outerwear',
    defaults={'name': 'Outerwear'}
)

# Add bomber
Product.objects.get_or_create(
    slug='block-bomber',
    defaults={
        'category': category,
        'name': '"BLOCK" Bomber',
        'price': 9760,
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

print("✅ Bomber added! Refresh your browser.")
