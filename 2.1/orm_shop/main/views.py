from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale


def cars_list_view(request):
    # получите список авто
    template_name = 'main/list.html'
    context = {
        'cars':Car.objects.all()
    }
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    template_name = 'main/details.html'
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        raise Http404()
    return render(request, template_name, {'car': car })  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        template_name = 'main/sales.html'
        car = Car.objects.get(id=car_id)
        return render(request, template_name, {'car': car,'sales':Sale.objects.filter (car=car) })  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
