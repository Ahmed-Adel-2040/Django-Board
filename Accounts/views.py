from django.shortcuts import render,redirect
from django.contrib.auth import login as Auth_Login
from .forms import SignUp
# Create your views here.
def signup(request):
    form = SignUp()
    if request.method=="POST":
        form=SignUp(request.POST)
        if form.is_valid():
            user=form.save()
            Auth_Login(request,user)
            return redirect("home")
    return render(request, 'signup.html', {'form': form})