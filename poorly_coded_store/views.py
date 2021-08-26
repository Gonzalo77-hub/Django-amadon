from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Count, Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    id_prod = float(request.POST["id"])
    product = Product.objects.get(id=id_prod)
    price_from_form = product.price
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

    return redirect("/checkout_page")
def check_final(request):
    context2 = {

            "orders": Order.objects.all(),
            "order_last": Order.objects.last(),
            "orders_total_price": Order.objects.all().aggregate(precio_total=Sum('total_price')),
            "order_total": Order.objects.all().aggregate(Cantidad=Count('quantity_ordered'))
    }
    return render(request, "store/checkout.html",context2 )