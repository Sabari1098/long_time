from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Department, Courses, Student


# from .forms import StudentForm


# Create your views here
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('new_page')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('register')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
                # messages.info(request,"User created successfully")
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def new_page(request):
    return render(request, 'new_page.html')


def form(request):
    depobj = Department.objects.all()
    couobj = Courses.objects.all()
    if request.method == 'POST':
            name = request.POST['name']
            dob = request.POST['dob']
            age = request.POST['age']
            gender = request.POST['gender']
            phone = request.POST['phone']
            mail = request.POST['mail']
            address = request.POST['address']
            # department = request.POST['department']
            # course = request.POST['course']
            purpose = request.POST['purpose']
            material = request.POST['material']
            if name == "" and dob == "" and age == "" and gender == "" and phone == "" and mail == "" and address == "" and material == "" and purpose == "":
                messages.info(request, "All field should be filled.")

            else:
                form_detail = Student(name=name, dob=dob, age=age, gender=gender, phone=phone, mail=mail,
                                      address=address,
                                      material=material, purpose=purpose)
                form_detail.save()
                return redirect('form')
    return render(request, 'form.html', {'department': depobj, 'course': couobj})
