from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            # Redirect to a success page.
            return redirect('admin_dashboard')
        else:
            # Return an 'invalid login' error message.
            return redirect('users:admin_users_list')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('admin_login')



@method_decorator([login_required(login_url="/admin/login")], name='dispatch')
class Dashboard(TemplateView):
    template_name = "accounts/dashboard.html"