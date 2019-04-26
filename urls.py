from django.urls import path
from . import views
#
urlpatterns = [
    path('', views.landingview, name='landingPage'),
    path('info', views.formview, name='formPage'),
    path('gender-chart', views.gender, name='gender'),
    path('rating-chart', views.product_rating, name='rating'),
    path('pie-chart', views.country_percentage, name='pie-chart')
]
