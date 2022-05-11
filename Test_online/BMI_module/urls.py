from django.urls import path
from . import views


urlpatterns = [
    path('calculate_bmi/', views.contactFormView, name='calculate_bmi'),
    path('Disease_group/', views.Disease, name='Disease_group'),
    path('show_foods/', views.show_food, name='show_foods'),
]
