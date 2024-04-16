from django.shortcuts import render

# Create your views here.

def hello_webpack(request):
    return render(request, 'backend/hello_webpack.html')