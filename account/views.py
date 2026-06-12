from django.shortcuts import redirect, render
from .forms import UserRegisterForm

# Create your views here.

def signup(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('account:login')  # Redirect to login page after successful registration
    else:
        form=UserRegisterForm()
    return render(request, 'templates/authPages/signup.html', {'form': form})