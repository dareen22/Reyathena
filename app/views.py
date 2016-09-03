from django.shortcuts import render, redirect, render_to_response 
from django.http import HttpResponse, HttpResponseRedirect
from app.models import Sport, Athlete, CustomeUserManager, CustomUser
from forms import ContactForm
from django.db import IntegrityError
from forms import CustomUserCreationForm, CustomUserLoginForm, ContactForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User


# Create your views here.

def sport_list(request):

    context = {}

    sports = Sport.objects.all()

    context['sports'] = sports

    return render(request, 'sport_list.html', context)

# def athlete_list(request):

#     context = {}

#     athletes = Athlete.objects.all()

#     context['athletes'] = athletes

#     return render (request, 'athlete_list.html', context)

def athlete_list(request, pk):

    context = {}

    sport = Sport.objects.get(pk=pk)

    context['sport'] = sport

    context['sport'] = Sport.objects.get(pk=pk)


    return render (request, 'athlete_list.html', context)

def athlete_detail(request, pk):

    context = {}

    context['athlete'] = Athlete.objects.get(pk=pk)

    #context['category'] = Category.objects.get(pk=pk)

    return render (request, 'athlete_detail.html', context)

def about_view(request):

  context = {}
  
  return render (request, 'about.html', context)   
  

def contact(request):
   context = {}
   form_class = ContactForm()
   context['form'] = form_class
   
   return render(request, 'contact.html', context)    



def signup(request):

  context = {}

  form = CustomUserCreationForm()

  context['form'] = form 

  if request.method == 'POST':
    
    form = CustomUserCreationForm(request.POST)

    if form.is_valid():

      print form.cleaned_data 
      # name = form.cleaned_data['name']
      email = form.cleaned_data.get('email', None)
      password = form.cleaned_data.get('password', None)


      try:
        form.save()
        # new_user = User.objects.create_user(email, password)
        context['valid'] = "Thank You For Signing Up and Welcome to Reyathena!"
        
        # auth_user = authenticate(username=email, password=password)
        # login(request, auth_user)

        return HttpResponseRedirect('/sport_list/')

      except IntegrityError as e:
        context['valid'] = "We know its annoying but, a User With That Name Already Exists"
        message = """
        We know its annoying but, a User With That Name Already Exists
        <a href= '/login_view/'>login<a>
        """

        return HttpResponse(message)
    else:
      context['valid'] = form.errors

  elif request.method == 'GET':
    context['valid'] = "Please join Reyathena and Sign Up!"

  return render (request, 'signup.html', context)


def login_view(request):

    context = {}
    context['form'] = CustomUserLoginForm()

    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        context['form'] = form

        if form.is_valid():
            email = form.cleaned_data.get('email', None)
            password = form.cleaned_data.get('password', None)
            auth_user = authenticate(username=email, password=password)

            try:
                login(request, auth_user)
            except Exception, e:
                print e
                message = """
                username or password incorrect, try again 
                <a href= '/login_view/'></a>
                """ 
                return HttpResponse(message) 
            return redirect ('/sport_list/')
            
    return render(request, 'login_view.html', context)




def logout_view(request):

  logout(request)

  return HttpResponseRedirect('/login_view/')  


def events_view(request):

  context = {}
  
  return render (request, 'tornaments.html', context) 

   


