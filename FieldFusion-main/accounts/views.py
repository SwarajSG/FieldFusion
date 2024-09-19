from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from .forms import RegisterForm
from .forms import RegistrationForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user is not None:
                user.set_password(form.cleaned_data['password1']) #hash the password
                # You should hash the password before saving in production
                user.save()
                return redirect('login')  # Redirect to a login page or login page
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


##def register(request):
    ##return render(request, 'register.html')  # Ensure this matches the file path

# def create_user(request):
#     user = User(name="Vijay Jagdale", age=21)
#     user.save()
