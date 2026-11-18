from django.shortcuts import render

def index(request):
    context = {
        'name': 'Rahul',
    }
    return render(request, 'home/index.html', context)