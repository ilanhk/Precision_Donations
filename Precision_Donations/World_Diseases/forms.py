from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from World_Diseases.models import Diseases, Research_labs, Donor, Funding, Images_or_Videos_of_disease, Deaths_sufferers_per_country_per_year


#DONOR SECTION

class Donorform(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('phone_number', 'address', 'city', 'country', 'profile_image')

    # class Donor(models.Model):
    #     user = models.OneToOneField(User, on_delete=models.CASCADE)
    #     phone_number = models.CharField(max_length=30)
    #     address = models.CharField(max_length=100)
    #     city = models.CharField(max_length=30)
    #     country = models.ForeignKey('Countries', on_delete=models.CASCADE)


# LAB SECTION
#
#   #all will include all fields from models research labs and funding bc they have relationship

class Labform(forms.ModelForm):
    class Meta:
        model= Research_labs
        exclude = ('user',)
            # ('lab_name', 'phone_number', 'company_website', 'address', 'city')

        # class Research_labs(models.Model):
        #     user = models.OneToOneField(User, on_delete=models.CASCADE)
        #     lab_name = models.CharField(max_length=50)
        #     disease = models.ForeignKey('Diseases', on_delete=models.CASCADE)
        #     phone_number = models.CharField(max_length=30)
        # company_website = models.CharField(max_length=100, null=True)
        #     address = models.CharField(max_length=100)
        #     city = models.CharField(max_length=30)
        #     country = models.ForeignKey('Countries', on_delete=models.CASCADE)

class LabFunding(forms.ModelForm):
    class Meta:
        model = Funding
        fields = '__all__'
            # ('amount_of_funding', 'year')

        # class Funding(models.Model):
        #     # annual_report_finiacial statement = ??? pdf
        #     #date_of_report = models.DateField()
        #     lab = models.ForeignKey('Research_labs', on_delete=models.CASCADE)
        #     amount_of_funding = models.FloatField()
        #     year = models.CharField(max_length=10, null=True)


#DISEASE SECTION

class Diseaseform(forms.ModelForm):
    class Meta:
        model = Diseases
        fields = ('name', 'causes', 'symptoms', 'diagnosis', 'symptoms', 'treatments')


class Disease_stats_form(forms.ModelForm):
    class Meta:
        model = Deaths_sufferers_per_country_per_year
        fields = ('deaths', 'num_sufferers', 'year')


class Imgvidform(forms.ModelForm):
    class Meta:
        model = Images_or_Videos_of_disease
        fields = ('link',)

# class Diseases(models.Model):
#     name = models.CharField(max_length=50)
#     causes = models.CharField(max_length=5000, null=True)
#     diagnosis = models.CharField(max_length=5000, null=True)
#     symptoms = models.CharField(max_length=5000, null=True)
#     treatments = models.CharField(max_length=5000, null=True)

# add disease attachments

# class Images_or_Videos_of_disease(models.Model):
#     link =models.CharField(max_length=1000) #??????????????????????? there is better
#     disease = models.ForeignKey('Diseases', on_delete=models.CASCADE)
#
# class Deaths_sufferers_per_country_per_year(models.Model):
#     country = models.ForeignKey('Countries', on_delete=models.CASCADE)
#     disease = models.ForeignKey('Diseases', on_delete=models.CASCADE)
#     deaths = models.IntegerField()
#     num_sufferers = models.IntegerField()
#     year = models.CharField(max_length=10, null=True)