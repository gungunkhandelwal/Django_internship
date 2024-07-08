from django.urls import path
from . views import *
urlpatterns = [
    path('signup/',signup,name='signup'),
    path('dashboard/',dashboard,name='dashboard'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout')

]
