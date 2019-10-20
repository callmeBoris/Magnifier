import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Search


BASE_YAHOO_URL = 'https://search.yahoo.com/search?p={}'

# Create your views here.
def home(request):
    return render(request, 'magnifier/index.html')


def results(request):

    search = request.POST.get('search')
    Search.objects.create(search_text=search)

    final_url = BASE_YAHOO_URL.format(quote_plus(search))
    
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    result_list = soup.find_all('div', {'class': 'algo-sr'})
    result_tilte = result_list[0].find(class_='compTitle').text
    result_url = result_list[0].find('a').get('href')
    
    print(result_tilte)
    print(result_url)

    return render(request, 'magnifier/results.html', {'search': search})