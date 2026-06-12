from django.shortcuts import get_object_or_404, render
from .models import Renting
# Create your views here.
def rent_success(request, rent_id):
    rent = get_object_or_404(
        Renting,
        id=rent_id
    )
    return render(
        request,
        'rentals/rent_succes.html',
        { 
            'renting': rent
        }
    )