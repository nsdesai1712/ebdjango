from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('detection/home_async', home_async, name='home_async'),
    path('detection/predict_syms', predict_lung_cancer_sym, name='predict_syms'),
]

