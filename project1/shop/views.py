from django.shortcuts import render
from django.http import Http404

# Create your views here.
products = [
    {
        'id':i,
        'title':f'Shop Item {i}',
        'desc':f'This is the description for item {i}'

    }
    for i in range(1 , 11)
]

def product_details(request , product_id):
    product = next(( item for item in products if item['id'] == product_id),None)
    if product is None:
        raise Http404("Product not found")
    return render(request ,  'shop/detail.html', {'product':product})