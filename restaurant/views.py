from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Menu, Booking
from django.http import HttpResponse, JsonResponse
from datetime import datetime, date
from django.core import serializers
from .forms import BookingForm
import json

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu_data})

def display_menu_item(request, pk=None):
    menu_item = Menu.objects.get(pk=pk) if pk else None
    return render(request, 'menu_item.html', {'menu_item': menu_item})

def reservations(request):
    req_date = request.GET.get('date')
    if req_date:
        bookings = Booking.objects.filter(reservation_date=req_date)
    else:
        bookings = Booking.objects.all()
    data = list(bookings.values('first_name', 'reservation_date', 'reservation_slot'))
    return JsonResponse(data, safe=False)

def book(request):
    form = BookingForm()
    today = date.today()
    bookings = Booking.objects.filter(reservation_date=today)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
        else:
            print("Form errors:", form.errors)
    return render(request, 'book.html', {
        'form': form,
        'bookings': bookings,
        'slot_range': range(1, 25),
        'today': today
    })

def get_available_slots(request):
    req_date = request.GET.get('date')
    if not req_date:
        return JsonResponse({'error': 'Missing date parameter'}, status=400)
    try:
        datetime.strptime(req_date, '%Y-%m-%d')
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid date format'}, status=400)
    all_slots = [f"{i:02d}:00" for i in range(0, 24)]
    booked_slots = Booking.objects.filter(reservation_date=req_date).values_list('reservation_slot', flat=True)
    available_slots = [slot for slot in all_slots if slot not in booked_slots]
    return JsonResponse({'available_slots': available_slots})

def get_bookings(request):
    req_date = request.GET.get('date')
    if not req_date:
        return JsonResponse({'error': 'Missing date parameter'}, status=400)
    try:
        datetime.strptime(req_date, '%Y-%m-%d')
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid date format'}, status=400)
    bookings = Booking.objects.filter(reservation_date=req_date)
    data = {
        'bookings': [
            {
                'first_name': b.first_name,
                'reservation_slot': b.reservation_slot
            }
            for b in bookings
        ]
    }
    return JsonResponse(data)