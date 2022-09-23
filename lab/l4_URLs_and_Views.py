# URLs and Views


#URL - pyt kym resurs v internet
# moje RegEx in URLs


# obekt request vyv views
#request.GET        # query params (?param1=value1&param2=value2)
#request.POST       # body of HTTP request
#
# def show_departments(request, *args, **kwargs):
#
#     order_by = request.GET.get('order_by', 'name')
#     body = f'path: {request.path}, ' \
#            f'args={args}, ' \
#            f'kwargs={kwargs}, ' \
#            f'order_by: {order_by}'
#
#     return HttpResponse(body)

# v browsera: http://127.0.0.1:8000/departments/?order_by=age
# pokazwa: path: /departments/, args=(), kwargs={}, order_by: age


# render function
# def show_departments(request, *args, **kwargs):
#     context = {
#         'method': request.method,
#         'order_by': request.GET.get('order_by', 'name'),
#     }
#     return render(request, 'departments/all.html', context)


# redirect
# def redirect_to_first_department(request):
#     possible_order_by = ['name', 'age', 'id']
#     order_by = choice(possible_order_by)
#     #to = f'/departments/?order_by={order_by}'
#     to = 'https://www.abv.bg/'
#     return redirect(to)


#named urls
#path('', show_departments, name='show departments'),
#slagame nakraq name

# def redirect_to_first_department(request):
#     return redirect('show departments')


# podavane na dopylnitelna info
# def redirect_to_first_department(request):
#     return redirect('details', department_id=13)


# views returning errors
"""
v settings.py ima DEBUG=True, ako go napravq False, ne pokazva greshki za potrebitelq

def show_not_found(request):
    return HttpResponseNotFound("Not...")


def show_not_found(request):
    status_code = 404
    return HttpResponse("Error", status=status_code)


def show_not_found(request):
    raise Http404("Nnnn...")


za da pokajem nasha stranica pravim 404.html v templates
kogato sprem debuga vijdame nashata stranica
"""






















