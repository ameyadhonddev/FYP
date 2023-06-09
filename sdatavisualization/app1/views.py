from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import JsonResponse 

# Create your views here.
@login_required(login_url='login')

def Homepage(request):
    return render (request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse('Password and confirm password should be same!')

        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
        #print(uname, email, pass1, pass2)



    return render (request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password = pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            return HttpResponse('Incorrect username or password')
    return render (request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def AdvSearch(request):
    #my_custom_sql()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM organization;")
        row = cursor.fetchall()
    #print(type(row))
    data = {"org": row}

    return render(request, 'advanced_search.html', data)

def my_custom_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchone()
        print(row)

    return row

def getDataset(request):
    print("request")
    return JsonResponse(request)