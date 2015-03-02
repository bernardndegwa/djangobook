from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from sections.models import Item
from django.core.context_processors import request

from sections.models import Item, List

# Create your views here.
def home_page(request):
    #item = Item()
    #item.text = request.POST.get('user_name', '')
    #item.save()
    
    #if request.method == 'POST':
        #new_user_text = request.POST['user_name']
        #Item.objects.create(text=request.POST['user_name'])
        #return redirect('sections/kamaus-only/')
    
    #else:
    #    new_user_text = ''    
        #return HttpResponse(request.POST['user_name'])
    #items = Item.objects.all()
    return render(request, 'home.html')

def view_section(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    #if request.method == 'POST':
        #new_user_text = request.POST['user_name']
        #Item.objects.create(text=request.POST['user_name'])
        
    
    return render(request, 'sections.html', {'items': items})

def new_user(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['user_name'], list=list_)
    return redirect('/sections/%d/' % (list_.id,))

def add_user(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['user_name'], list=list_)
    return redirect('/sections/%d' %(list_.id,))

    
