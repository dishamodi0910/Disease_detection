from django import forms
from django import views
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('diabetes/',views.diabetes,name='diabetes'),
    path('result_diabetes/',views.result_diabetes,name='result_diabetes'),
    path('heart/',views.heart,name='heart'),
    path('result_heart/',views.result_heart,name='result_heart'),
    path('parkinsons/',views.parkinsons,name='parkinsons'),
    path('result_parkinsons/',views.result_parkinsons,name='result_parkinsons'),
    path('dengue/',views.dengue,name='dengue'),
    path('result_dengue/',views.result_dengue,name='result_dengue'),
    path('home/',views.home,name='home'),
    path('signup_login/',views.signup_login,name='signup_login'),
    path('aboutus/',views.aboutus,name='aboutus'),
]
