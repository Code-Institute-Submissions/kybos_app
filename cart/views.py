
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect, reverse
from models import cartItem
from products.models import Terrarium
from django.contrib.auth.decorators import login_required
from payments.forms import MakePayment
from django.contrib import messages
from django.template.context_processors import csrf
from django.conf import settings


import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required(login_url="/log_in")
def add_to_cart(request, id):
    add_item=get_object_or_404(Terrarium, pk=id)
    quantity=int(request.POST.get('quantity'))
    try:
        cartitem = cartItem.objects.get(user=request.user, product=add_item)
        cartitem.quantity += quantity
    except cartItem.DoesNotExist:
        cartitem = cartItem(
            user = request.user,
            product = add_item,
            quantity = quantity,
        )
    cartitem.save()
    return redirect(reverse('cart_user'))

def remove_from_cart(request, id):
    cartItem.objects.get(id=id).delete()
    return redirect(reverse('cart_user'))


@login_required(login_url="log_in")
def cart_user(request):
    cartitems = cartItem.objects.filter(user=request.user)
    total = 0
    for item in cartitems:
        total += item.quantity * item.product.price_big
    if request.method == "POST":
        form = MakePayment(request.POST)
        if form.is_valid():
            try:
                costumer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError, e:
                messages.error(request, 'Your card was declined')

            if costumer.paid:
                messages.success(request, 'You have successfully paid')
                cartItem.objects.filter(user=request.user).delete()
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Unable to take your payment')
        else:
            messages.error(request, 'We were unable to take your payment with that card')

    else:
        if len(cartitems) == 0:
            return render(request, 'empty_cart.html')
        form = MakePayment()

    args = {'form':form,
            'items': cartitems,
            'total': total,
            'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'cart.html', args)

def thank_page(request):
    return render(request, "thanks.html")
