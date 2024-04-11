from django.urls import path
from . import views
from .views import custom_permission_denied_view

urlpatterns = [
     path('login/',views.login_user,name='login'),
     path('candidte-register/',views.candidateregister,name='register'),
     path('register/',views.register,name='register-user'),
     path('hr-register/',views.hrregister,name='register-hr'),
     path('logout/',views.logoutUser,name='logout'),
]

handler403 = custom_permission_denied_view
