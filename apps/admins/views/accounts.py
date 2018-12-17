from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            # Redirect to a success page.
            return redirect('users:users_list')
        else:
            # Return an 'invalid login' error message.
            return redirect('users:users_list')
    return render(request, 'accounts/login.html')