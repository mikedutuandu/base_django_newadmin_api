from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView,ListView
from django.contrib.auth.models import User



class UserListView(ListView):
    queryset = User.objects.all()
    template_name = "admin/users/list.html"
