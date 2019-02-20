from django.urls import include, path

from apps.fronts.views import classroom, students, teachers

urlpatterns = [

    #path('admin/', admin.site.urls),

    #accounts
    #path('ad/login', auth_views.LoginView.as_view(template_name='admin/acounts/login.html')),


    #users

     #url(r'^ad/users/$', UserListView.as_view(), name='users_list'),






    path('', include('apps.fronts.urls')),
    path('admin/', include('apps.admins.urls')),



]


