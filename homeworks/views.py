from django.shortcuts import render


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
