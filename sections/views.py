from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['user_name'])
    return render(request, 'home.html')