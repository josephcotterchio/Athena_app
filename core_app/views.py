
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
# Define the home view
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Industry, Skill
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from bs4 import BeautifulSoup
import requests


def search(request):
    print(request)
    page = requests.get(
        "https://ca.indeed.com/jobs?q=Junior+Developer&l=Toronto%2C+ON")
    soup = BeautifulSoup(page.content, 'html5lib')
    alltitles = soup.find_all("h2", class_="title")
    print(alltitles)
    return render(request, 'search.html/', {'alltitles': alltitles})


def home(request):
    return render(request, 'home.html')


def profile(request):
    profile = Profile.objects.get(user=request.user)
    # skills_profile_doesnt_have = Skill.objects.exclude(
    #     id__in=profile.currentskill_set.all().values_list('id'))

    # We need skill template forms to be rendered in the template, and we need industry form to render in ProfileUpdate
    # skill_form = SkillForm()
    # industry_form=IndustryForm()

    return render(request, 'main_app/profile.html', {
        'profile': profile,
        # '_form': skill_form,
        # 'skills': skills_profile_doesnt_have
    })


def apptracker(request):
    return render(request, 'main_app/apptracker.html')


def profile_form(request):
    return render(request, 'main_app/profile_form.html')


def savedjobs(request):
    return render(request, 'main_app/savedjobs.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html/', context)
