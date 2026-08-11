from apps.catalog.models import Category, Product

def seed_initial_data():
    try:
        if Product.objects.exists():
            return

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
                'image': 'products/black_tshirt_main.jpg',
            },
            {
                'name': '"VEYM: ECHO OF CHAOS"',
                'slug': 'veym-echo-of-chaos',
                'price': 2800,
                'category': cat_tops,
                'description': 'плотность - 180гр/м2\n100% хлопок',
                'image': 'products/white_tshirt_main.jpg',
            },
            {
                'name': '"VEYM: WHITE SHADOW"',
                'slug': 'veym-white-shadow',
                'price': 2500,
                'category': cat_tshirts,
                'description': 'плотность - 180гр/м2\n100% хлопок',
                'image': 'products/white_tshirt_main.jpg',
            },
            {
                'name': '"VEYM: BLACK SHADOW"',
                'slug': 'veym-black-shadow',
                'price': 2500,
                'category': cat_tshirts,
                'description': 'плотность - 180гр/м2\n100% хлопок',
                'image': 'products/black_tshirt_main.jpg',
            },
        ]

        for p in products:
            Product.objects.get_or_create(
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
    except Exception as e:
        print(f"Error seeding data: {e}")
