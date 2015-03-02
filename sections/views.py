from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from sections.models import Item

# Create your views here.
def home_page(request):
    #item = Item()
    #item.text = request.POST.get('user_name', '')
    #item.save()
    
    if request.method == 'POST':
        #new_user_text = request.POST['user_name']
        Item.objects.create(text=request.POST['user_name'])
        return redirect('/')
    
    #else:
    #    new_user_text = ''    
        #return HttpResponse(request.POST['user_name'])
    items = Item.objects.all()
    return render(request, 'home.html', {'items':items})