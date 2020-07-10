from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H3CrbDwaOGgZ3driENulN22GJQvWdg57GxbiLobaAee83s0SOGUFQQA4u0mbDwoRfotwe9w0NwlDim9bFU1q1cK00yNj7GFSv',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)