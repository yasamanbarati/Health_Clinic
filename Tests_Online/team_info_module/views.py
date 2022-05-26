from django.shortcuts import render
from django.views import View
from . import models


def team_Info_view(request):
    info = models.MembersInfo.objects.all()
    return render(request, 'group_info.html', {'members': info})

