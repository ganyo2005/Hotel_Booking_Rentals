from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Contact_Us


def contact_us(request):

    if request.method == "POST":

        fullname = request.POST.get('name')

        business_name = request.POST.get('business_name')

        email = request.POST.get('email')

        phone_number = request.POST.get('phone')

        service_type = request.POST.get('service')

        message = request.POST.get('message')


        Contact_Us.objects.create(

            fullname=fullname,

            business_name=business_name,

            email=email,

            phone_number=phone_number,

            service_type=service_type,

            message=message

        )

        return redirect('hotels:home')


    return render(
        request,
        'hotels/contact.html'
    )

