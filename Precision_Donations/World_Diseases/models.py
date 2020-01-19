from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Donars section

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    country = models.ForeignKey('Countries', on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_image', blank=True, default='profile_image/blank-profile.png')

    def __repr__(self):
        return f"Donar: {self.user.username} {self.user.first_name} {self.user.last_name}  {self.user.email} {self.phone_number} {self.address} {self.city} {self.profile_image}"


# Research Labs section

# list of research Laboritories
class Research_labs(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)  # change to one_to_one when everything works and delete table
    lab_name = models.CharField(max_length=50)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, null=True)
    disease = models.ForeignKey('Diseases', on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=30)
    company_website = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    country = models.ForeignKey('Countries', on_delete=models.CASCADE)
    lab_image = models.ImageField(upload_to='profile_image', blank=True, default='profile_image/default_lab_image.jpg')

    def __str__(self):
        return self.lab_name

    def __repr__(self):
        return f"Research_lab_sign_up:{self.lab_name} {self.lab_image}"


# Funding of each lab
class Funding(models.Model):
    # annual_report_finiacial statement = ??? pdf
    # date_of_report = models.DateField()
    lab = models.ForeignKey('Research_labs', on_delete=models.CASCADE)
    amount_of_funding = models.FloatField()
    year = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Funding:  {self.lab.name} "


# World Diseases Section


class Deaths_sufferers_per_country_per_year(models.Model):
    country = models.ForeignKey('Countries', on_delete=models.CASCADE)
    disease = models.ForeignKey('Diseases', on_delete=models.CASCADE)
    deaths = models.IntegerField()
    num_sufferers = models.IntegerField()
    year = models.CharField(max_length=10, null=True)

    def __repr__(self):
        return f"Deaths_sufferers_per_country_per_year: {self.deaths} {self.num_sufferers}{self.year}"


# list of countries
class Countries(models.Model):
    name = models.CharField(max_length=50)
    offical_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Countries: {self.name} "


# rate of spread
class Rate_of_spread(models.Model):
    disease = models.ForeignKey('Diseases', on_delete=models.CASCADE)
    rate = models.FloatField()  # active field
    year = models.CharField(max_length=10, null=True)

    def __repr__(self):
        return f"Rate_of_spread: {self.rate} {self.year}"


# images or videos of disease
class Images_or_Videos_of_disease(models.Model):
    link = models.CharField(max_length=1000)  # ??????????????????????? there is better
    disease = models.ForeignKey('Diseases', on_delete=models.CASCADE)

    def __repr__(self):
        return f"Images_or_Videos_of_disease: {self.link}"


# list of Diseases
class Diseases(models.Model):
    name = models.CharField(max_length=50)
    causes = models.CharField(max_length=5000, null=True)
    diagnosis = models.CharField(max_length=5000, null=True)
    symptoms = models.CharField(max_length=5000, null=True)
    treatments = models.CharField(max_length=5000, null=True)

    # cure yes or no if effective

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Diseases: {self.name}"


# categories of world problems
class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Categories: {self.name}"



class Donor_wish_list(models.Model):
    donor= models.ForeignKey('Donor', on_delete=models.CASCADE)
    lab=models.ForeignKey('Research_labs', on_delete=models.CASCADE)

    def __repr__(self):
        return f"Categories: {self.donor} {self.lab}"
