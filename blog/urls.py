from django.urls import include,path
from  django.conf.urls.static import static
from . import views
from blog.views import *

urlpatterns = [

    path('home/',views.home),
    path('hello/',views.hello),
    path('blog_name/',views.blog_name),
    path('index/',views.index),
    path('sp/',views.sp),




]