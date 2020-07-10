from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('home')

    else:
            form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form': form})