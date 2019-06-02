from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import Order
from .models import Item

@login_required
def item_list(request):
    object_list = Item.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_items = []
    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_items = [item.item for item in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_items': current_order_items
    }

    return render(request, "items/item_list.html", context)
