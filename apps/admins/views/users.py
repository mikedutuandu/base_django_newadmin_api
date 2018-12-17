from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView,ListView
from apps.fronts.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required(login_url="/admin/login")], name='dispatch')
class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'users/list.html'
