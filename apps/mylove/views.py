from django.shortcuts import redirect, render
from django.views.generic import TemplateView


def love(request):
    return render(request, 'love.html')