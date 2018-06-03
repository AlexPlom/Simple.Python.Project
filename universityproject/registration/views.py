from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            return redirect('/posts')
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {'form': form})


    #return render(request,'registration/login.html')

def logout(request):
    return render(request,'registration/logout.html')