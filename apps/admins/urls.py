from django.urls import include, path

from .views import users,accounts

urlpatterns = [
    # path('', classroom.home, name='home'),

    path('login', accounts.login_view, name='admin_login'),
    path('logout', accounts.logout_view, name='admin_logout'),
    path('', accounts.Dashboard.as_view(), name='admin_dashboard'),

    path('users/', include(([
        path('', users.UserListView.as_view(), name='admin_users_list'),

    ], 'users'), namespace='users')),
]