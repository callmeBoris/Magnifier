import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Search


BASE_WEBDESIGNERDEPOT_URL = 'https://www.webdesignerdepot.com/?s={}'

# Create your views here.
def home(request):
    return render(request, 'magnifier/index.html')


def results(request):

    search = request.POST.get('search')
    Search.objects.create(search_text=search)

    final_url = BASE_WEBDESIGNERDEPOT_URL.format(quote_plus(search))
    
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    result_list = soup.find_all('article', {'class': 'list-post'})
    
    results = []

    for result in result_list:
        result_category = result.find(class_='hp-category').text
        result_tilte = result.find(class_='main-post-title').text
        result_excerpt = result.find(class_='hp-excerpt').text
        result_url = result.find('a').get('href')
        result_image = result.find('img').get('src')

        results.append((result_category, result_tilte, result_url, result_excerpt, result_image))

    return render(request, 'magnifier/results.html', {'search': search, 'results': results})