from django.shortcuts import render
from homeworks.forms import TicketOrderForm


def hw_19_01(request):
    strings = [request.POST.get("str_01", ''),
               request.POST.get("str_02", ''),
               request.POST.get("str_03", '')]

    strings.sort(key=len)
    search_result = 'Input at least one string, please.'
    if strings[-1] != '':
        search_result = f"The longest string: {strings[-1]}"

    return render(request,
                  'hw1901.html',
                  context={"search_result": search_result})


def hw_19_02(request):
    chosen_date = request.POST.get("form1__date", '')
    result_message = ''
    if chosen_date != '':
        year, month, day = chosen_date.split("-")
        if day == '01' and month == '01':
            result_message = f'Happy New {year} Year!'
        else:
            result_message = f'Chosen date:  {chosen_date}'

    return render(request,
                  'hw1902.html',
                  context={"result_message": result_message})


def hw_20(request):
    if request.method == 'GET':
        order_form = TicketOrderForm()
        return render(request, "order.html", context={'form': order_form})
    elif request.method == 'POST':
        order_form = TicketOrderForm(request.POST)
        if order_form.is_valid():
            pass_amount = int(request.POST.get('passengers_cnt'))
            message = f"Total price: {100 if pass_amount == 1 else 100 * 2 * pass_amount}$"
            return render(request,
                          'order.html',
                          context={'form': order_form,
                                   'message': message})
        else:
            message = "Wrong input. Please, check."
            return render(request,
                          'order.html',
                          context={'form': order_form,
                                   'message': message})
