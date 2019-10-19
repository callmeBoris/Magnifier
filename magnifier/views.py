from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request, 'magnifier/index.html')


def results(request):
    search = request.POST.get('search')
    return render(request, 'magnifier/results.html', {'search': search})