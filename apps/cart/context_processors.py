from services.cart import CartService

def cart_processor(request):
    """Provide cart total and count to all templates"""
    cart = CartService.get_or_create_cart(request)
    return {
        'cart_count': CartService.get_cart_count(cart),
        'cart_total': CartService.get_cart_total(cart),
        'cart_items': cart.items.all()
    }
