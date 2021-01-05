from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.
from . import models
from .forms import Donorform, Labform, LabFunding, Diseaseform, Disease_stats_form, Imgvidform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F, Sum, Q  # to do calculations in the queries
import os


def index(request):
    return render(request, "index.html")


@login_required
def home(request, number=0):
    return render(request, "home.html")


# Disease section
@login_required
def diseases_list(request):
    affected_countries = models.Countries.objects.all()
    dlist = models.Diseases.objects.all()
    dlist = dlist.annotate(gdeaths=Sum(F('deaths_sufferers_per_country_per_year__deaths')),
                           gsuffer=Sum(F('deaths_sufferers_per_country_per_year__num_sufferers')),
                           gfunding=Sum(F('research_labs__funding__amount_of_funding'))
                           )

    def yearly_stats(year='2020', country='World'):
        stats = dlist.filter(deaths_sufferers_per_country_per_year__year=year, research_labs__funding__year=year)
        most_deaths_least_funding_list = stats.order_by('-gdeaths', 'gfunding')

        if country == "World":
            return most_deaths_least_funding_list
        else:
            return most_deaths_least_funding_list.filter(deaths_sufferers_per_country_per_year__country__name=country)

    if request.method == "POST":
        year = request.POST.get('year')
        location = request.POST.get('location')
        diseases_list_dict = {
            'diseases': yearly_stats(year, location),
            'countries': affected_countries,
        }
        return render(request, "list_of_Diseases.html", diseases_list_dict)
    else:

        diseases_list_dict = {
            'diseases': yearly_stats(),
            'countries': affected_countries,
        }

        return render(request, "list_of_Diseases.html", diseases_list_dict)


@login_required
def disease_details(request, id):
    disease = models.Diseases.objects.get(id=id)
    imagesvids = models.Images_or_Videos_of_disease.objects.filter(disease=disease).first()
    list_of_labs = models.Research_labs.objects.filter(disease=id).all()

    return render(request, "Disease_details.html", {'disease': disease, 'imagesvids': imagesvids, 'labs': list_of_labs})


def add_new_disease(request):
    form = Diseaseform()
    image=Imgvidform()
    if request.method == 'POST':
        form = Diseaseform(request.POST)
        image = Imgvidform(request.POST)
        if form.is_valid() and image.is_valid():
            disease = form.save(commit=False)
            img_disease = image.save(commit=False)
            disease.user = request.user
            img_disease.user =request.user
            disease.save()
            img_disease.save()
            return redirect('newdisease_statistics')

        else:
            form = Diseaseform()
            image = Imgvidform()
    return render(request, 'form_addnew_disease.html', {'form': form, 'image':image})


def new_disease_stats(request):
    form = Disease_stats_form(initial={'lab': request.user.research_labs})
    if request.method == 'POST':
        form = Disease_stats_form(request.POST)
        if form.is_valid():
            funding = form.save(commit=False)
            funding.user = request.user
            funding.save()
            return redirect('labform')
        else:
            form = Disease_stats_form()
    return render(request, 'form_for_newdisease_stats.html', {'form': form})


# Labs list section
@login_required
def labs_list(request, id):
    list_of_labs = models.Research_labs.objects.filter(disease=id).all()

    return render(request, "list_of_research_labs.html", {'labs': list_of_labs})


# return redirect('lab_edit_details')

@login_required
def lab_details(request, id):
    lab = models.Research_labs.objects.get(id=id)
    return render(request, "Research_lab_details.html", {'lab': lab})


# sign up section
def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(username, raw_password)
            user = authenticate(username=username, password=raw_password)
            print(user)
            login(request, user)
            return redirect('choose')
        else:
            print(form.errors)
            form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def choice(request):
    print('hey choice')
    return render(request, "profilesetup.html")


def donor_details_fill(request):
    form = Donorform()
    if request.method == 'POST':
        form = Donorform(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.user = request.user
            donor.save()
            return redirect('home')

        else:
            form = Donorform()
    return render(request, 'form_for_donor.html', {'form': form})


def lab_details_fill(request):
    form = Labform()
    if request.method == 'POST':
        form = Labform(request.POST, request.FILES)
        if form.is_valid():
            lab = form.save(commit=False)
            lab.user = request.user
            lab.save()
            return redirect('labfundingform')

        else:
            form = Labform()
    return render(request, 'form_for_lab.html', {'form': form})


def lab_edit_details(request, id):
    lab = models.Research_labs.objects.get(id=id)
    user = lab.user
    if request.method == 'POST':
        form = Labform(request.POST, request.FILES, instance=lab)
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.save()
        form.save()
        return redirect('research_lab_details', lab.id)
    else:
        form = Labform(instance=lab)
    return render(request, "lab_edit_form.html", {'form': form, 'lab': lab})


def funding_details_fill(request):
    form = LabFunding(initial={'lab': request.user.research_labs})
    if request.method == 'POST':
        form = LabFunding(request.POST)
        if form.is_valid():
            funding = form.save(commit=False)
            funding.user = request.user
            funding.save()
            return redirect('research_lab_details', request.user.research_labs.id)
        else:
            form = LabFunding()
    return render(request, 'form_for_lab_funding.html', {'form': form})


# Donor Section

@login_required
def Donor_profile(request, id):
    donor = models.Donor.objects.get(id=id)

    return render(request, "donor_profile.html", {'donor': donor})


def donor_edit_details(request, id):
    donor = models.Donor.objects.get(id=id)
    user = donor.user
    if request.method == 'POST':
        form = Donorform(request.POST, request.FILES, instance=donor)
        print(request.FILES)
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.save()
        form.save()
        return redirect('donor_profile', donor.id)
    else:
        form = Donorform(instance=donor)
    return render(request, "donor_edit_form.html", {'form': form, 'donor': donor})


# navbar section
def navbar(request, id):
    donor = models.Donor.objects.get(user_id=id)
    lab = models.Research_labs.objects.get(user_id=id)

    user_type_dict = {
        'donor': donor,
        'lab': lab,
    }

    return render(request, "base.html", user_type_dict)


# Search Bar Section
@login_required
def search(request):
    if request.method != 'POST':
        return render(request, 'search.html')
    text = request.POST.get('search', '')

    lab_list = models.Research_labs.objects.filter(Q(lab_name__icontains=text))

    donor_list = models.Donor.objects.filter(Q(user__first_name__icontains=text) | Q(user__last_name__icontains=text) | Q(user__username__icontains=text))

    disease_list = models.Diseases.objects.filter(Q(name__icontains=text))
    print(lab_list,donor_list,disease_list, text)
    return render(request, 'search.html',
                  {'lab_list': lab_list, 'donor_list': donor_list, 'disease_list': disease_list, 'text':text})


# for Climate change app concept
def climate_change_concept(request):
    return render(request, "climate_change.html")


# for world hunger app concept
def world_hunger_concept(request):
    return render(request, "world_hunger.html")
