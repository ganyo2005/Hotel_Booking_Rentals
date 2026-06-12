from datetime import datetime
from decimal import Decimal

from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib import messages


from rent_booking.models import Renting
from .models import Rental
# Create your views here.
def rentals_home(request):
    
    search = request.GET.get('search')
    rentals = Rental.objects.first()


    if search:

        rentals = rentals.filter(
            Q(name__icontains=search) |
            Q(location__icontains=search) |
            Q(description__icontains=search)
        )

    return render(request, 'rentals/rentals.html', {'rentals': rentals})





def rental_details(request):
    name = request.GET.get('name', 'Ambulance')

    rental = get_object_or_404(
        Rental,
        name=name
    )

    return render(
        request,
        'rentals/rent_details.html',
        {
            'rental': rental
        }
    )





def rent(request,rental_id):
    
    rent= get_object_or_404(
        Rental,
        id=rental_id
    )

    # BOOKING FOR
  
        
    if request.method == "POST":
        destination= request.GET.get('name')
        price=request.GET.get('price')
        if price is None:
            price = 0
            
        new_price = Decimal(price)

        check_in = request.POST.get('check_in')

        check_out = request.POST.get('check_out')

        quantity = request.POST.get('quantity')
        customer_number = request.POST.get("customer_number")


        item = request.GET.get('item')  # Get room type from query parameters

       
        if not check_in:
            messages.error(request, "Check in date is required.")
            return redirect(request.path)

        if not check_out:
            messages.error(request, "Check out date is required.")
            return redirect(request.path)

        



        if not customer_number:
            messages.error(request, "Phone number is required.")
            return redirect(request.path)
        check_in_date = datetime.strptime( check_in,
            "%Y-%m-%d"
           )

        check_out_date = datetime.strptime(
            check_out,
            "%Y-%m-%d"
        )
        extra_charges = int(100)
        total_price = new_price   + extra_charges
        days = (check_out_date - check_in_date).days

        renting=Renting.objects.create(

            user=request.user,

            rent=rent,

            item=item,
            price=new_price,

            destination=destination,

            check_in=check_in,

            check_out=check_out,

            quantity=quantity,

            total_price=total_price

        )
        print(f"this is {renting.id}")
        return render(request, 'rentals/rent_succes.html', {'renting': renting, 'total_price': total_price, 'extra_charges': extra_charges})
    return render(
        request,
        'rentals/rent_book.html',
        {
            'rental': rent,'item': request.GET.get('item'),
              'destination': request.GET.get('name'), 'price': request.GET.get('price')  # Pass room type and price to the template
        }
    )


