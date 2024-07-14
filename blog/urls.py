from django.urls import path
from . views import *
urlpatterns = [
    path('add_blog/',add_blog,name='add_blog'),
    path('update_blog/<int:id>',update_blog,name='update_blog'),
     path('delete_blog/<int:id>',delete_blog,name='delete_blog'),
     path ('display_blog/',display_blog,name='display_blog'),
]
