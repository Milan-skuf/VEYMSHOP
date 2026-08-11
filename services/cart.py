from django.shortcuts import get_object_or_404
from apps.cart.models import Cart, CartItem
from apps.catalog.models import Product

class CartService:
    @staticmethod
    def get_or_create_cart(request):
        """Get or create cart for current session/user"""
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            cart, created = Cart.objects.get_or_create(session_key=session_key)
        return cart

    @staticmethod
    def add_item(request, product_id, quantity=1, size='M'):
        """Add item to cart or update quantity if exists"""
        cart = CartService.get_or_create_cart(request)
        product = get_object_or_404(Product, id=product_id)
        
        # Check if item with same product AND size already exists
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            size=size,
            defaults={'quantity': quantity, 'price': product.price}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        return cart

    @staticmethod
    def remove_item(request, item_id):
        """Remove item from cart"""
        cart = CartService.get_or_create_cart(request)
        CartItem.objects.filter(id=item_id, cart=cart).delete()
        return cart

    @staticmethod
    def update_item_quantity(request, item_id, quantity):
        """Update quantity of cart item"""
        if quantity < 1:
            return CartService.remove_item(request, item_id)
            
        cart = CartService.get_or_create_cart(request)
        cart_item = CartItem.objects.get(id=item_id, cart=cart)
        cart_item.quantity = quantity
        cart_item.save()
        return cart

    @staticmethod
    def get_cart_total(cart):
        """Calculate total price"""
        return sum(item.quantity * item.price for item in cart.items.all())

    @staticmethod
    def get_cart_count(cart):
        """Get total item count"""
        return sum(item.quantity for item in cart.items.all())
