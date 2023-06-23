from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Clonedata/index.html')

def about(request):
    return render(request, 'Clonedata/about.html')