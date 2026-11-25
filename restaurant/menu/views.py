from django.shortcuts import render, redirect
from .models import MenuItem
from .forms import MenuItemForm

def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu_list.html', {'items': items})

def add_item(request):
    form = MenuItemForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('menu_list')
    return render(request, 'menu/item_form.html', {'form': form})