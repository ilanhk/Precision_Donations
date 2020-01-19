from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('listofdiseases/', views.diseases_list, name='listofdiseases'), #always use the name for the html urls
    path('disease_details/<int:id>', views.disease_details, name='disease_details'),
    path('list_of_research_labs/<int:id>', views.labs_list, name='list_of_research_labs'),
    path('research_lab_details/<int:id>', views.lab_details, name='research_lab_details'),
    path('signup/', views.signup, name='signup'),
    path('choose/', views.choice, name='choose'),
    path('donorform/', views.donor_details_fill, name='donorform'),
    path('labform/', views.lab_details_fill, name='labform'),
    path('labfundingform/', views.funding_details_fill, name='labfundingform'),
    path('newdisease/', views.add_new_disease, name='newdisease'),
    path('newdisease_statistics/', views.new_disease_stats, name='newdisease_statistics'),
    path('lab_edit_details/<int:id>', views.lab_edit_details, name='lab_edit_details'),
    path('donor_edit_details/<int:id>', views.donor_edit_details, name='donor_edit_details'),
    path('donor_profile/<int:id>', views.Donor_profile, name='donor_profile'),
    path('climate_change/', views.climate_change_concept, name='climate_change'),
    path('world_hunger/', views.world_hunger_concept, name='world_hunger'),
    path('search/', views.search, name='search'),


]