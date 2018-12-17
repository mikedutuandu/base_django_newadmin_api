from django.urls import include, path

from .views import users,accounts

urlpatterns = [
    # path('', classroom.home, name='home'),

    path('login', accounts.login, name='login'),

    path('users/', include(([
        path('', users.UserListView.as_view(), name='users_list'),

    ], 'users'), namespace='users')),
]