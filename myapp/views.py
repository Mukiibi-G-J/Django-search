from django.shortcuts import render



def home(request):
    return render(request, 'myapp/home.html')



def new_search(request):
    search = request.POST.get('search')
    print(search)
    stuff_frontend = {
        'search': search
    }
    return render(request, 'myapp/new_search.html', stuff_frontend)
