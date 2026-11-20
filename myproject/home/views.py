from django.shortcuts import render, redirect
from .models import Student

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        city = request.POST.get("city")

        Student.objects.create(name=name, age=age, city=city)
        return redirect("index")          # dobara page pe bhejo (duplicate submit se bachne ke liye)

    students = Student.objects.all()
    return render(request, "home/index.html", {"students": students})