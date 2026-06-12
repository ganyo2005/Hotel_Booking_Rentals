from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.shortcuts import render
from .models import Hotel
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Hotel
from bookings.models import Hotel_Booking as Booking
from datetime import datetime
from django.db.models import Q
from django.contrib import messages
from bookings.models import Hotel_Booking
from decimal import Decimal
from rent_booking.models import Rental

def home(request):
    search = request.GET.get('search')
    hotels = Hotel.objects.all()

        
    rentals = Rental.objects.all()
    rentalsSingle= Rental.objects.get(name="Ambulance")


    if search:

        rentals = rentals.filter(
            Q(name__icontains=search) |
            Q(location__icontains=search) |
            Q(description__icontains=search)
        )

        hotels = hotels.filter(
            Q(name__icontains=search) |
            Q(location__icontains=search) |
            Q(description__icontains=search)
        )

    return render(request, 'hotels/home.html',{
        'hotels': hotels,'rentals': rentals, 'rentalsSingle': rentalsSingle
    })

def success(request,success_id):
    success_id = get_object_or_404(
        Hotel_Booking,
        id=success_id
    )

    return render(
        request,
        'hotels/succes.html',
        {
            'booking': success_id
        }
    )
def about_us(request):
    return render(
        request,
        'hotels/about_us.html'
    )

def hotel_detail(request, hotel_id):

    hotel = get_object_or_404(
        Hotel,
        id=hotel_id
    )
    # BOOKING FORM

    return render(
        request,
        'hotels/hotel_detalis.html',
        {
            'hotel': hotel
        }
    )


def book_hotel(request,book_id):

    hotel = get_object_or_404(
        Hotel,
        id=book_id
    )

    room_type = request.GET.get('room_type')

    # BOOKING FORM

    if request.method == "POST":
        user=request.POST.get('user')

        check_in = request.POST.get('check_in')

        check_out = request.POST.get('check_out')

        guests = request.POST.get('guests')

        customer_number = request.POST.get(
            'customer_number'
        )


        # ERROR HANDLING

        if not check_in or not check_out:

            messages.error(
                request,
                "Please select check in and check out dates"
            )

            return render(
                request,
                'hotels/book_hotel.html',
                {
                    'hotel': hotel,
                    'room_type': room_type
                }
            )

        if not customer_number:

            messages.error(
                request,
                "Please enter your phone number"
            )

            return render(
                request,
                'hotels/book_hotel.html',
                {
                    'hotel': hotel,
                    'room_type': room_type
                }
            )


        # DATE CONVERSION

        check_in_date = datetime.strptime(
            check_in,
            "%Y-%m-%d"
        )

        check_out_date = datetime.strptime(
            check_out,
            "%Y-%m-%d"
        )


        # DATE VALIDATION

        if check_out_date <= check_in_date:

            messages.error(
                request,
                "Check out date must be after check in date"
            )

            return render(
                request,
                'hotels/book_hotel.html',
                {
                    'hotel': hotel,
                    'room_type': room_type
                }
            )


        # TOTAL DAYS

        days = (
            check_out_date - check_in_date
        ).days


        # ROOM PRICE

        # ROOM PRICE
        room_price = None
        
        if room_type == hotel.room1_name:
        
            room_price = hotel.room1_price
        
        elif room_type == hotel.room2_name:
        
            room_price = hotel.room2_price
        
        elif room_type == hotel.room3_name:
        
            room_price = hotel.room3_price
        
        elif room_type == hotel.room4_name:
        
            room_price = hotel.room4_price

        # TOTAL PRICE

        # CHECK IF ROOM PRICE EXISTS
        
        if room_price is None:
        
            messages.error(
                request,
                "Selected room is not available"
            )
        
            return render(
                request,
                'hotels/book_hotel.html',
                {
                    'hotel': hotel,
                    'room_type': room_type
                }
            )
        
        
        # BASE PRICE
        
        base_price = days * room_price
        
        
        # EXTRA GUEST CHARGES
        
        guests = int(guests)
        
        extra_charge = Decimal("50.00") + Decimal((guests - 1) * 30)
        
        
        # FINAL TOTAL PRICE
        
        total_price = base_price + extra_charge

        # SAVE BOOKING

        booking = Booking.objects.create(

            user=user,

            hotel=hotel,

            room_type=room_type,

            check_in=check_in,

            check_out=check_out,

            guests=guests,

            customer_number=customer_number,

            total_price=total_price
            

        )


        # SUCCESS MESSAGE

        messages.success(
            request,
            "Booking created successfully"
        )


        return render(
        request,
        'hotels/succes.html',
        {
            'booking': booking,
            'extra_charge': extra_charge
        } )


    return render(
        request,
        'hotels/book_hotel.html',
        {
            'hotel': hotel,
            'room_type': room_type
        }



    )

