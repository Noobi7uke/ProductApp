from django.urls import path

from  .views import authentication_form_view,auth_login_view,auth_register_view
from django.contrib.auth.views import logout_then_login
app_name = 'authentication'

urlpatterns = (
    path('', authentication_form_view, name='auth_form'),
    path('register/', auth_register_view, name='auth_register'),
    path('login/', auth_login_view, name='auth_login'),
    path('logout/',logout_then_login, {'login_url': '/auth'})
)