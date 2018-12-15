from django.urls import include, path

from apps.fronts.views import classroom, students, teachers

urlpatterns = [
    path('', include('apps.fronts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]



#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#
#     #accounts
#     path('ad/login', auth_views.LoginView.as_view(template_name='admin/acounts/login.html')),
#
#
#     #users
#
#     # url(r'^ad/users/$', UserListView.as_view(), name='users_list'),
# ]


