from django.urls import include, path

from apps.mylove import views

urlpatterns = [
    path('', views.love, name='love'),

]