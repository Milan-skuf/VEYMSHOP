import os
import shutil
from django.conf import settings
from apps.catalog.models import Category, Product

def seed_initial_data():
    try:
        # Copy original 3D character photos if they exist locally on Desktop
        src_photos = r"C:\Users\ИВАН\Desktop\VEYMSHOP_ALL_PHOTOS"
        dst_photos = os.path.join(settings.BASE_DIR, 'static', 'products')
        os.makedirs(dst_photos, exist_ok=True)
        
        for char_name in ['char1.png', 'char2.png', 'char3.png', 'char4.png']:
            src = os.path.join(src_photos, char_name)
            dst = os.path.join(dst_photos, char_name)
            if os.path.exists(src) and not os.path.exists(dst):
                try:
                    shutil.copy2(src, dst)
                except Exception as e:
                    print(f"Error copying {char_name}: {e}")

        cat_tshirts, _ = Category.objects.get_or_create(
            slug='t-shirts',
            defaults={'name': 'T-Shirts'}
        )
        cat_tops, _ = Category.objects.get_or_create(
            slug='tops',
            defaults={'name': 'Tops'}
        )

        products = [
            {
                'name': 'VEYM "SCRAP"',
                'slug': 'veym-scrap',
                'price': 2800,
                'category': cat_tops,
                'description': 'плотность - 180гр/м2\n100% хлопок\nоверлок швы',
                'image': 'products/char1.png',
            },
            {
                'name': '"VEYM: ECHO OF CHAOS"',
                'slug': 'veym-echo-of-chaos',
                'price': 2800,
                'category': cat_tops,
                'description': 'плотность - 180гр/м2\n100% хлопок',
                'image': 'products/char2.png',
            },
            {
                'name': '"VEYM: WHITE SHADOW"',
                'slug': 'veym-white-shadow',
                'price': 2500,
                'category': cat_tshirts,
                'description': 'плотность - 180гр/м2\n100% хлопок',
                'image': 'products/char3.png',
            },
            {
                'name': '"VEYM: BLACK SHADOW"',
                'slug': 'veym-black-shadow',
                'price': 2500,
                'category': cat_tshirts,
                'description': 'плотность - 180гр/м2\n100% хлопок',
                'image': 'products/char4.png',
            },
        ]

        for p in products:
            prod, created = Product.objects.get_or_create(
                slug=p['slug'],
                defaults={
                    'name': p['name'],
                    'price': p['price'],
                    'category': p['category'],
                    'description': p['description'],
                    'image': p['image'],
                    'is_active': True,
                }
            )
            if prod.image != p['image']:
                prod.image = p['image']
                prod.save()
    except Exception as e:
        print(f"Error seeding data: {e}")
