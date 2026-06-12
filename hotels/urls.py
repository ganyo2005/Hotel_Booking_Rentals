from django.urls import path
from .views import  about_us, home, hotel_detail,book_hotel, success

app_name = 'hotels'
urlpatterns = [
    path('', home, name='home'),
    path('hotels/<int:hotel_id>/', hotel_detail, name='hotel_detail'),
    path('book_hotel/<int:book_id>/',book_hotel,name='book_hotel'),
    path('success/<int:success_id>/',success,name='success'),
    path('about/',about_us,name='about_us'),

]