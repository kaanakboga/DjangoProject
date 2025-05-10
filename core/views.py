from django.shortcuts import render

# Create your core here.
def index(request):
    return render(request, 'index.html')