import os
import shutil
from django.conf import settings
from apps.catalog.models import Category, Product, ProductImage

def seed_initial_data():
    try:
        src_dir = r"C:\Users\ИВАН\Desktop\VEYMSHOP_ALL_PHOTOS"
        dst_products = os.path.join(settings.BASE_DIR, 'static', 'products')
        dst_videos = os.path.join(settings.BASE_DIR, 'static', 'videos')
        os.makedirs(dst_products, exist_ok=True)
        os.makedirs(dst_videos, exist_ok=True)
        
        # Copy photos from Desktop folder if present
        if os.path.exists(src_dir):
            for file_name in os.listdir(src_dir):
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    src_file = os.path.join(src_dir, file_name)
                    dst_file = os.path.join(dst_products, file_name)
                    if not os.path.exists(dst_file):
                        try:
                            shutil.copy2(src_file, dst_file)
                        except Exception:
                            pass

        # Copy video if exists
        video_src_candidates = [
            r"F:\0130.mp4",
            os.path.join(src_dir, "0130.mp4"),
            r"C:\Users\ИВАН\Desktop\0130.mp4"
        ]
        for v_src in video_src_candidates:
            if os.path.exists(v_src):
                v_dst = os.path.join(dst_videos, "banner.mp4")
                if not os.path.exists(v_dst):
                    try:
                        shutil.copy2(v_src, v_dst)
                    except Exception:
                        pass
                break

        cat_tshirts, _ = Category.objects.get_or_create(
            slug='t-shirts',
            defaults={'name': 'T-Shirts'}
        )
        cat_tops, _ = Category.objects.get_or_create(
            slug='tops',
            defaults={'name': 'Tops'}
        )

        detailed_description = """VEYM | DIGITAL CONCEPT — Характеристики

Стиль и крой:
• Силуэт: Приталенный крой (Slim Fit), подчеркивающий фигуру.
• Дизайн: Вертикальные рельефные швы по бокам для создания структурного, футуристичного образа. Глубокие проймы и акцентированная линия плеч.
• Детали: Крупный высококачественный принт VEYM на груди. Авторские элементы деструкции (дизайнерские потертости и микро-дыры), придающие вещи уникальный винтажный вид.

Материалы и плотность:
• Состав: 100% натуральный хлопок премиум-класса. Ткань дышит и приятна к телу.
• Плотность: 180 г/м² — оптимальная толщина: материал достаточно плотный, чтобы держать форму и не просвечивать.

Качество исполнения:
• Усиленные плечевые швы для предотвращения деформации при носке."""

        # Clean extra ProductImages so no secondary images exist
        ProductImage.objects.all().delete()

        products_data = [
            {
                'name': 'VEYM "SCRAP"',
                'slug': 'veym-scrap',
                'price': 2800,
                'category': cat_tops,
                'description': detailed_description,
                'image': 'products/char1.png',
            },
            {
                'name': '"VEYM: ECHO OF CHAOS"',
                'slug': 'veym-echo-of-chaos',
                'price': 2800,
                'category': cat_tops,
                'description': detailed_description,
                'image': 'products/char2.png',
            },
            {
                'name': '"VEYM: WHITE SHADOW"',
                'slug': 'veym-white-shadow',
                'price': 2500,
                'category': cat_tshirts,
                'description': detailed_description,
                'image': 'products/char3.png',
            },
            {
                'name': '"VEYM: BLACK SHADOW"',
                'slug': 'veym-black-shadow',
                'price': 2500,
                'category': cat_tshirts,
                'description': detailed_description,
                'image': 'products/char4.png',
            },
        ]

        for p in products_data:
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
            prod.description = p['description']
            prod.image = p['image']
            prod.save()

    except Exception as e:
        print(f"Error seeding data: {e}")
