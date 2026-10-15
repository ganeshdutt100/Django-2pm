from django.shortcuts import render

# Create your views here.
def shop_view(request, category=None):
    all_products=[
        # watch 
        {
            'name': 'Apple Watch Ultra 2',
            'category': 'watch',
            'price': '₹89,900',
            'image': 'https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=600&auto=format&fit=crop&q=80'
        },
        {
            'name': 'Samsung Galaxy Watch 6',
            'category': 'watch',
            'price': '₹29,999',
            'image': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=80'
        },
        {
            'name': 'Fossil Gen 6 Smartwatch',
            'category': 'watch',
            'price': '₹18,495',
            'image': 'https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=600&auto=format&fit=crop&q=80'
        },
        # phone 
        {
            'name': 'iPhone 16 Pro',
            'category': 'phone',
            'price': '₹1,19,900',
            'image': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600&auto=format&fit=crop&q=80'
        },
        {
            'name': 'Samsung Galaxy S24 Ultra',
            'category': 'phone',
            'price': '₹1,29,999',
            'image': 'https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=600&auto=format&fit=crop&q=80'
        },
        {
            'name': 'OnePlus 12 5G',
            'category': 'phone',
            'price': '₹64,999',
            'image': 'https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=600&auto=format&fit=crop&q=80'
        },
    ]

    if category in ['watch','phone']:
        products =[p for p in all_products if p['category'] == category  ]
        active_tab  = 'all'
    else:
        products  = all_products,
        active_tab = 'all'    

    context = {
        'products':products,
         'active_tab':active_tab         
    }    
    return render(request , 'shop/products.html',context)