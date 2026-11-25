from django.shortcuts import render, redirect
from .models import Student

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.http import url_has_allowed_host_and_scheme

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        city = request.POST.get("city")

        Student.objects.create(name=name, age=age, city=city)
        return redirect("index")          # dobara page pe bhejo (duplicate submit se bachne ke liye)

    students = Student.objects.all()
    return render(request, "home/index.html", {"students": students})


    @login_required
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        city = request.POST.get("city")
        Student.objects.create(name=name, age=age, city=city)
        return redirect("index")

    students = Student.objects.all()
    return render(request, "index.html", {"students": students})


@login_required
def delete_student(request, id):
    if request.method == "POST":
        student = get_object_or_404(Student, id=id)
        student.delete()
    return redirect("index")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()          # user database me save
            login(request, user)        # seedha login bhi kar do
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = request.GET.get("next", "")
            if url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("login")