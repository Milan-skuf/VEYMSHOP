from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from services.cart import CartService

class CartDetailView(View):
    def get(self, request):
        cart = CartService.get_or_create_cart(request)
        total = CartService.get_cart_total(cart)
        return render(request, 'cart/cart_detail.html', {
            'cart': cart,
            'total': total
        })

class CartAddView(View):
    def post(self, request, product_id):
        try:
            size = request.POST.get('size', 'M')
            quantity = int(request.POST.get('quantity', 1))
            cart = CartService.add_item(request, product_id, quantity=quantity, size=size)
            cart_count = CartService.get_cart_count(cart)
            
            # Return success toast notification and update counter via OOB
            return HttpResponse(
                f'<div class="fixed top-20 right-4 bg-green-500 text-white px-6 py-3 rounded shadow-lg z-50" '
                f'x-data="{{show: true}}" x-show="show" x-init="setTimeout(() => show = false, 2000)">'
                f'✓ Added to cart! ({cart_count} items)'
                f'</div>'
                f'<span id="cart-counter" hx-swap-oob="true">{cart_count}</span>',
                headers={'HX-Trigger': 'cartUpdated'}
            )
        except Exception as e:
            return HttpResponse(
                f'<div class="fixed top-20 right-4 bg-red-500 text-white px-6 py-3 rounded shadow-lg z-50">'
                f'Error: {str(e)}'
                f'</div>',
                status=400
            )

class CartRemoveView(View):
    def post(self, request, item_id):
        try:
            cart = CartService.remove_item(request, item_id)
            total = CartService.get_cart_total(cart)
            # Re-render the cart
            return render(request, 'cart/cart_detail.html', {
                'cart': cart,
                'total': total
            })
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=400)

class CartUpdateView(View):
    def post(self, request, item_id):
        try:
            quantity = int(request.POST.get('quantity', 1))
            cart = CartService.update_item_quantity(request, item_id, quantity)
            total = CartService.get_cart_total(cart)
            # Re-render the cart
            return render(request, 'cart/cart_detail.html', {
                'cart': cart,
                'total': total
            })
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=400)
