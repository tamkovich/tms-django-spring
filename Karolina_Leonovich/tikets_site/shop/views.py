from django.shortcuts import render
from .forms import OrderForm

def order_tikets(request):
    error = ""
    quantity_from_form = 0
    total_price = 0
    if request.method == "POST":
        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            form_order.save()
            data = form_order.cleaned_data
            quantity_from_form = int(data['quantity'])
            total_price = quantity_from_form * 100
        else:
            error = "Введите нормально данные"
    form_order = OrderForm()
    return render(request, "shop/order.html", {
        "form_order": form_order,
        "error": error,
        "quantity_from_form": quantity_from_form,
        "total_price": total_price,
    })
