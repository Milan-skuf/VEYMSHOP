from apps.catalog.models import Category

def categories_processor(request):
    return {
        'catalog_categories': Category.objects.all().order_by('name')
    }
