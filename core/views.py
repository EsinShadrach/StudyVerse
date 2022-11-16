from django.shortcuts import render
from .models import Items
from django.db.models import Q
# Create your views here.
def homepage(request):
    # q = request.GET.get('search') if request.GET.get('search') != None else ''
    if request.GET.get('search') != None:
        q = request.GET.get('search')
    else:
        q = ''
    itemsx = Items.objects.filter(
        Q(name__icontains = q) |
        Q(tag__icontains = q)
    )
    count = itemsx.count()
    items_count = f'found {count}'
    context = {
        'items': itemsx,
        'items_count':items_count,
        'query':q
    }
    return render(request, 'core/index.html', context)
    
    
def createCard(request):
    context = {}
    return render(request, 'core/addcard.html', context)
    
def detailedView(request, pk):
    items = Items.objects.get(id=pk)
    context = {
        'item':items
    }
    return render(request, 'core/detailedpage.html', context)