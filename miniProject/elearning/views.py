from django.shortcuts import render

# Create your views here.
def course_list(request):
    courses=[
       {
           'title':'Python Full Stack MasterClasses',
           'instructor':'Tech Academy',
           'duration':'50hr',
           'price':'2000',
           'badge':'Bestseller',
            'image':'https://images.unsplash.com/photo-1672922310200-fff31138251e?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
       },
       {
          'title':'Java Full Stack MasterClasses',
          'instructor':'Tech Academy',
          'duration':'70hr',
          'price':'4000',
          'badge':'Popular',
          'image':'https://images.unsplash.com/photo-1588239034647-25783cbfcfc1?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
              },
        
         {
           'title':'Complete  Mern Stack MasterClasses',
           'instructor':'Tech Academy',
           'duration':'90hr',
           'price':'5000',
           'badge':'Trending',
            'image':'https://plus.unsplash.com/premium_photo-1685086785223-485f800ce410?w=1200&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D'
       },      

    ]