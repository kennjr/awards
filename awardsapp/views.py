from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"title": ''}
    return render(request, 'awardsapp/index.html', context)
