from django.shortcuts import render
from requests.compat import quote_plus
from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests
from . models import Search

BASE_URL="https://chicago.craigslist.org/search/?query={}"

def home(request):
    return render(request, 'myapp/home.html')



def new_search(request):
    search = request.POST.get('search')
    Search.objects.create(search=search)
    print(quote_plus(search))
    final_url = BASE_URL.format(quote_plus(search)) 
    response = requests.get(final_url)
    status = response.status_code
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
                # post_title = soup.find_all('a',{'class': 'result-title'})
                # print(post_title[0].text)
    post_listing = soup.find('li',{'class':'result-row'})
    post_title = post_listing[0].find(class_='result-title').text
    post_url = post_listing.find('a').get('href')
    price = post_listing.find(class_='result-price').text
    print(post_title[0].get('href'))
    post_results = soup
    # print(data)
    # print(data)
    print(final_url)
    # print(status)
    # print(search)
    stuff_frontend = {
        'search': search
    }
    return render(request, 'myapp/new_search.html', stuff_frontend)
