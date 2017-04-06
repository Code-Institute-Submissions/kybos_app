from django.shortcuts import render, get_object_or_404, redirect, reverse
from payments.forms import MakePayment
from products.models import Terrarium
from django.contrib import messages
from django.conf import settings
from django.template.context_processors import csrf

import stripe

# Create your views here.


def payment_check_out(request, id):
    if request.method == 'POST':
        form = MakePayment(request.POST)
        if form.is_valid():
            try:
                payment = get_object_or_404(Terrarium, pk=id)
                costumer = stripe.Charge.create(
                    amount = int(Terrarium.price * 100),
                    currency = 'EUR',
                    description = Terrarium.title,
                    card = form.cleaned_data['stripe_ide'],
                )
            except stripe.error.CardError, e:
                messages.error(request, 'Your card was declined')

            if costumer.paid:
                messages.success(request, 'You have succesfully paid')
                return redirect(reverse('home'))

            else:
                messages.error(request, 'Unable to take the payment' )
        else:
            messages.error(request, 'Unable to take the payment with that card')

    else:
        form = MakePayment()
        payment = get_object_or_404(Terrarium, pk=id)

    args = {'form':form, 'publishable': settings.STRIPE_PUBLISHABLE, 'payment':payment}
    args.update(csrf(request))
    return render(request, 'check_out.html', args)


