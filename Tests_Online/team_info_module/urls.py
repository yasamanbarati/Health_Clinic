from django.urls import path
from . import views


urlpatterns = [
    path('group_info/', views.team_Info_view, name='group_info'),
    ]
