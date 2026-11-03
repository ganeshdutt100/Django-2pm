from django.shortcuts import render , redirect

# Create your views here.
user_list=[
        {
            'name':"Tahendra",
            'age':23,
           "feedback":"python classes "
        }
    ]
def home_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        feedback = request.POST.get('feedback')


        new_user ={
            "name":name,
            "age":int(age) if age else 0,
            "feedback":feedback
        }
        user_list.append(new_user)
        return redirect('home')


    


    context={
        'users':user_list
#       'users':[
#         {
#             'name':"Tahendra",
#             'age':23,
#             'skills':["Python","React","HTML","CSS"]
#         },
#          {
#                 'name':"Rahul",
#                 'age':21,
#                 'skills':["Java","SQL","HTML","CSS"]
#         },
# 
#         {
#           'name':"Priya",
#           'age':22,
#            'skills':["Node","SQL","HTML","CSS"]
#         },        
#       ]
    }
    # return render(request,"demo/index.html",context)
    return render(request,"demo/feedback.html",context)
