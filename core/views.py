from django.shortcuts import render

def cover_page(request):
    return render(request, 'core/cover.html')

def country_view(request, country_name):
    return render(request, f'core/{country_name}.html', {'country': country_name})
