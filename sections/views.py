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
        #return redirect('/sections/kamaus-only')
    
    #else:
    #    new_user_text = ''    
        #return HttpResponse(request.POST['user_name'])
    items = Item.objects.all()
    return render(request, 'home.html', {'items':items})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    #items = Item.objects.filter(list=list_)
    return render(request, 'section.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['user_name'], list=list_)
    return redirect('sections/%d' % (list_.id,))
    #return redirect(view_list(request, list_id=list_))
    
def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['user_name'], list=list_)
    return redirect('sections/%d' % (list_.id,))





