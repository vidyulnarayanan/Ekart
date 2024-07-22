from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from django.contrib import messages
from products.models import product

#Create your views here.
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
    context={'cart':cart_obj}
    return render(request,'cart.html',context)

def remove_item_from_cart(request,pk):
    item=OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

def checkout_cart(request):
    if request.POST:
        try:
            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get('total'))
            # Debug: print the total
            print(f"Total: {total}")

            order_obj = Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )         
            if order_obj: 
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                status_message = "Your order is processed. Your items will be delivered"
                messages.success(request, status_message)
            else:
                status_message = "Unable to proceed. No items in cart"
                messages.error(request, status_message)
        except Order.DoesNotExist:
            status_message = "Unable to proceed. No items in cart"
            messages.error(request, status_message)
        except Exception as e:
            status_message = "An error occurred while processing your order"
            messages.error(request, status_message)
        
        return redirect('cart')
    


def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj, created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product_obj=product.objects.get(pk=product_id)
        ordered_item,created=OrderedItem.objects.get_or_create(
            product=product_obj,
            owner=cart_obj,
        )
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            ordered_item.quantity=ordered_item.quantity+quantity
            ordered_item.save()

    return redirect('cart')




