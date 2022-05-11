from django.shortcuts import render

# Create your views her


def index_page(request):
    return render(request, 'index.html')


def site_header_component(request):
    return render(request, 'shared/site_header_component.html')


def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html')

