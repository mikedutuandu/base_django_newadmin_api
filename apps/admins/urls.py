from django.urls import include, path

from .views import users

urlpatterns = [
    # path('', classroom.home, name='home'),

    path('users/', include(([
        path('', users.UserListView.as_view(), name='users_list'),

    ], 'users'), namespace='users')),
]