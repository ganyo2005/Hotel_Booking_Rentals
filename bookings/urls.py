from django.urls import path
from . import views
app_name='booking'
urlpatterns = [

    path(
        'order_history/',
        views.order_history,
        name='booking_order_history'
    ),
    # path('booking',views.booking,name='booking')

]