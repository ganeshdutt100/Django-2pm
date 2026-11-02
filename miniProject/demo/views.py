from django.shortcuts import render

# Create your views here.
def home_view(request):
    context={
      'users':[
        {
            'name':"Tahendra",
            'age':23,
            'skills':["Python","React","HTML","CSS"]
        },
         {
                'name':"Rahul",
                'age':21,
                'skills':["Java","SQL","HTML","CSS"]
        },

        {
          'name':"Priya",
          'age':22,
           'skills':["Node","SQL","HTML","CSS"]
        },        
      ]
    }
    return render(request,"demo/index.html",context)