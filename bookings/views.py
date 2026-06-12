from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Hotel_Booking
from .models import Hotel_Booking as Booking
from django.db.models import Q

# # def order_history(request):

# #     bookings = Hotel_Booking.objects.filter(
# #         user='full_name',
# #     ).order_by('-created_at')

# #     return render(
# #         request,
# #         'hotels/booking_order_history.html',
# #         {
# #             'bookings': bookings
# #         }
#     )


def order_history(request):
    search = request.GET.get('search')
    bookings = Booking.objects.all()

    if search:

        bookings = bookings.filter(
            Q(user__icontains=search) 
        )
    return render(request, 'hotels/booking_order_history.html', {
        'bookings': bookings
    })
