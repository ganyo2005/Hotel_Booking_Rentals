from django.urls import path

from rent_booking.views import rent_success
from .views import rent, rental_details, rentals_home

app_name = 'rentals'
urlpatterns = [
    path('', rentals_home, name='rentals_home'),
    path('rent/<int:rental_id>/', rent, name='rent'),
    path('rent_success/<int:rent_id>/', rent_success, name='rent_success'),
    path('rent_details/', rental_details, name='rent_details'),
]
