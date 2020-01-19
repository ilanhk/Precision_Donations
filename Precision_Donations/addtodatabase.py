import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Precision_Donations.settings')
import django
django.setup()

from faker import Faker
from World_Diseases.models import Countries, Diseases, Deaths_sufferers_per_country_per_year, Research_labs, Images_or_Videos_of_disease, Funding, Categories, User
from datetime import timedelta    #this makes it possible to add days to a previous saved date
import random
import pycountry
from bs4 import BeautifulSoup
import json
import requests
from django.contrib.auth.models import User

faker=Faker()

# to add all countries
# for q in pycountry.countries:
#     country = Countries(name=q.name)
#     country.save()





#list of Diseases

# lupus = Diseases(name='Lupus',
#                  causes='Doctors dont know exactly what causes lupus. They think genetics, hormones, and your environment may be involved.'
#                         ' Your body’s immune system protects you from bacteria, viruses, and other foreign invaders that can make you sick. '
#                         'But if you have lupus, your immune system also mistakenly attacks and damages your bodys own tissues, too. Diseases that do this are called autoimmune diseases.'
#                         'You could be born with a gene that makes you more likely to get lupus. Then you might be exposed to something in your environment, and that triggers the disease.'
#                         'But even if both of these things come together, that still doesnt mean you’ll get lupus. That’s why it’s so hard for doctors to figure out what causes it. '
#                         'What researchers do know is there are certain things that make you more likely to get it, including your heredity, gender, race, and even previous illnesses',
#
#                  diagnosis='Lupus is a difficult disease to diagnose, because its symptoms can be vague. And unlike some other diseases,'
#                            ' it cannot be diagnosed with a single lab test. However, when certain clinical criteria are met, '
#                            'lab tests can help confirm a diagnosis of lupus. Blood work and other tests can also help monitor the disease and show '
#                            'the effects of treatment.',
#                  symptoms='The symptoms you have depend on what areas of your body the lupus is affecting. But the most common ones include: Intense fatigue, Fever, Severe joint pain and muscle aches, '
#                           'Skin rash on the face or body, Extreme sun sensitivity, Weight loss, Chest pain on taking a deep breath, Nose, mouth, or throat sores, Enlarged lymph nodes, Poor circulation in fingers and toes, Bald patches and hair loss. '
#                           'Less common symptoms include: Confusion, Seizures, Anemia, Dizziness and Headaches. Most likely they will show up every now and then, or in what your doctor might call “flares.” Your symptoms will often get worse and then get better. Some could totally go away, but others might not improve at all.',
#                  treatments='There is no cure. However there are treatments that can extend a persons life but the side effects are detramental to a persons life and living standards. Flares may still happen that can put them in hostpital for days our weeks, which can seriously prevent them to work in the work force.'
#                  )
# lupus.save()
# response = requests.get('https://disease-info-api.herokuapp.com/diseases')
# data = json.loads(response.content)
#
# for i in range(47):
#     data = json.loads(response.content)
#
#     name=data['diseases'][i]['name']
#     causes=data['diseases'][i]['transmission']
#     diagnosis=data['diseases'][i]['diagnosis']
#     symptoms=data['diseases'][i]['symptoms']
#     treatments=data['diseases'][i]['treatment']
#
#     list_to_clean = [name, causes, diagnosis, symptoms, treatments]
#     cleaned_list =[]
#
#     for string in list_to_clean:
#         if string != None:
#             string = string.strip()
#             if "- WHO" in string:
#                 string=string.replace("- WHO", "")
#         elif string == None:
#             string = 'None'
#
#         cleaned_list.append(string)
#
#     disease=Diseases(name=cleaned_list[0], causes=cleaned_list[1], diagnosis=cleaned_list[2], symptoms=cleaned_list[3],
#     treatments=cleaned_list[4])
#     disease.save()


# for number of deaths and sufferers per year
# for i in range(1,49):
#     number_deaths_sufferers = Deaths_sufferers_per_country_per_year(
#         country=random.choice(Countries.objects.all()),
#         disease=Diseases.objects.get(id=i),
#         deaths=random.randint(10, 300000),
#         num_sufferers=random.randint(100, 1000000),
#         year='2017'
#     )
#     number_deaths_sufferers.save()

# faker.year_between(start_year="-3y", end_date="today") maybe use insttead

# for labs
# for i in range(1,49):
#      lab = Research_labs(
#          lab_name=faker.company(),
#          disease=Diseases.objects.get(id=i),
#          phone_number=faker.phone_number(),
#          company_website=faker.url(),
#          address=faker.address(),
#          city=faker.city(),
#          user_id=1,
#          country=random.choice(Countries.objects.all())
#      )
     # lab.save()

# to make fake users
# for i in range(300):
#     user = User.objects.create_user(username=f'{faker.first_name()}{i}{i}{i}' , password='Batman12345')
#     user.save()


# for i in range(1,194):
#     Research_labs.objects.filter(user_id=1).update(user_id=User.objects.get(id=(i+15)))

# x = 16
# for lab in Research_labs.objects.all():
#     lab.user = User.objects.get(id=x)
#     lab.save()
#     x += 1





# for funding
# for i in range(1, 194):
#     funding = Funding(lab=Research_labs.objects.get(id=i), amount_of_funding=random.randint(1000, 10000000), year='2017')
#     funding.save()



# class Funding(models.Model):
#     # annual_report_finiacial statement = ??? pdf
#     # date_of_report = models.DateField()
#     lab = models.ForeignKey('Research_labs', on_delete=models.CASCADE)
#     amount_of_funding = models.FloatField()
#     year = models.CharField(max_length=10, null=True)
#
# rabies =Images_or_Videos_of_disease(
#     link='https://images.theconversation.com/files/210502/original/file-20180315-104659-lubzum.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=496&fit=clip',
#     disease=Diseases.objects.get(id=1))
# malaria =Images_or_Videos_of_disease(
#     link='https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwiN1MLVrvLmAhWGblAKHVGFB0EQjRx6BAgBEAQ&url=https%3A%2F%2Fwww.thelivemirror.com%2Fnew-drug-approved-radical-cure-malaria%2F&psig=AOvVaw2li-FHbbJXcZO5UjCWuJIS&ust=1578516573275167',
#     disease=Diseases.objects.get(id=2))
# lassafever =Images_or_Videos_of_disease(
#     link='https://bukunmisdiary.files.wordpress.com/2016/01/lassa-fever-virus.jpg?w=727&h=546',
#     disease=Diseases.objects.get(id=3))
# tb =Images_or_Videos_of_disease(
#     link='https://cdn.the-scientist.com/assets/articleNo/66278/aImg/33044/tb.jpg',
#     disease=Diseases.objects.get(id=4))
# measles =Images_or_Videos_of_disease(
#     link='https://dynamicmedia.zuza.com/zz/m/original_/4/5/4572dfbf-3f1a-4e6d-9c99-cbda99c3fccb/tumblr_mn9k9xIJAr1qz72ywo1_1280___Gallery.jpg',
#     disease=Diseases.objects.get(id=5))
# meningcoccolmeningitus =Images_or_Videos_of_disease(
#     link='https://www.sanofi.com/-/media/Project/One-Sanofi-Web/Websites/Global/Sanofi-COM/Common/img/Vaccines/MeningococcalMeningitis/40yearsFighting.jpg?h=1614&la=en&w=1174&hash=22474DB5E5CDC1A833E558939162FF71',
#     disease=Diseases.objects.get(id=6))
# chik =Images_or_Videos_of_disease(
#     link='https://im.indiatimes.in/facebook/2018/Oct/weve_already_witnessed_17311_cases_of_chikungunya_this_year_heres_what_else_you_should_know_1539179915.jpg?h=420&w=800&cc=1',
#     disease=Diseases.objects.get(id=7))
# plague =Images_or_Videos_of_disease(
#     link='https://images.ctfassets.net/cnu0m8re1exe/6sWV2Iq2GMO1jtYeESoYS1/20d3f74a65493e3142c96db4af030d59/file-20191107-10905-609qr4.jpg?w=650&h=433&fit=fill',
#     disease=Diseases.objects.get(id=8))
# aids=Images_or_Videos_of_disease(
#     link='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSt29peAUefMwjxZ7rp3dzrwBr5Yk1Tk50Jtp6f2zb5VqaF5etL&s',
#     disease=Diseases.objects.get(id=9))
# forget1 =Images_or_Videos_of_disease(
#     link='https://www.nursinginpractice.com/sites/default/files/styles/articledesktopcontained/public/article/Vaccination%20web.jpg?itok=uuxHTvjT',
#     disease=Diseases.objects.get(id=10))
# pneumia =Images_or_Videos_of_disease(
#     link='https://images.medicinenet.com/images/illustrations/pneumonia.gif',
#     disease=Diseases.objects.get(id=11))
# rubella =Images_or_Videos_of_disease(
#     link='https://thenativeantigencompany.com/wp-content/uploads/2019/05/shutterstock_781768672.jpg',
#     disease=Diseases.objects.get(id=12))
# poliomyelitis =Images_or_Videos_of_disease(
#     link='https://img.medscapestatic.com/pi/meds/ckb/98/44398tn.jpg',
#     disease=Diseases.objects.get(id=13))
# hepb =Images_or_Videos_of_disease(
#     link='https://image.shutterstock.com/image-illustration/liver-hepatitis-b-infection-highlighted-260nw-1103225852.jpg',
#     disease=Diseases.objects.get(id=14))
# buruliulcer=Images_or_Videos_of_disease(
#     link='http://services.epnet.com/getimage.aspx?imageiid=7516',
#     disease=Diseases.objects.get(id=15))
# hepe =Images_or_Videos_of_disease(
#     link='https://i0.wp.com/www.lifebeyondhepatitisc.com/wp-content/uploads/2019/09/bigstock-Hepatitis-E-Viral-Infection-247374850-e1568915255101.jpg?resize=830%2C553&ssl=1',
#     disease=Diseases.objects.get(id=16))
# hepa =Images_or_Videos_of_disease(
#     link='https://cdn.prod-carehubs.net/n1/802899ec472ea3d8/uploads/2019/05/shutterstock_1122823709_Fotor-16x9-1024x576.jpg',
#     disease=Diseases.objects.get(id=17))
# forget2 =Images_or_Videos_of_disease(
#     link='https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png',
#     disease=Diseases.objects.get(id=18))
# soiltrans=Images_or_Videos_of_disease(
#     link='https://www.asm.org/ASM/media/Article-Images/2019/April/Helminths2-4-26-19.png?ext=.png',
#     disease=Diseases.objects.get(id=19))
# foodborntrem =Images_or_Videos_of_disease(
#     link='https://www.who.int/images/default-source/imported/foodborne-trematodiases-jpg.jpg?sfvrsn=3f9ed163_0',
#     disease=Diseases.objects.get(id=20))
# ebola =Images_or_Videos_of_disease(
#     link='https://psmag.com/.image/t_share/MTI3NTgyNDM3NTg3ODUwNTE0/ebola1.jpg',
#     disease=Diseases.objects.get(id=21))
# hepc =Images_or_Videos_of_disease(
#     link='https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/articles/health_tools/future_with_hepatitis_c_slideshow/getty_rm_illustration_of_hepatitis_c.jpg',
#     disease=Diseases.objects.get(id=22))
# yellowfever =Images_or_Videos_of_disease(
#     link='https://www.undispatch.com/un-content/uploads/2016/05/Screen-Shot-2016-05-12-at-1.35.31-PM.png',
#     disease=Diseases.objects.get(id=23))
# dengue =Images_or_Videos_of_disease(
#     link='https://www.internationalglobalhealth.com/upload/Dengue-Fever-banner.jpg',
#     disease=Diseases.objects.get(id=24))
# trachoma =Images_or_Videos_of_disease(
#     link='data:image/png;base64,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',
#     disease=Diseases.objects.get(id=25))
# chagas =Images_or_Videos_of_disease(
#     link='https://www-tc.pbs.org/wgbh/nova/media/images/triatomine.width-800.jpg',
#     disease=Diseases.objects.get(id=26))
# lymphaticfil =Images_or_Videos_of_disease(
#     link='https://previews.123rf.com/images/drmicrobe/drmicrobe1805/drmicrobe180500002/101015574-leg-of-a-person-with-elephantiasis-or-lymphatic-filariasis-and-close-up-view-of-microfilariae-in-blo.jpg',
#     disease=Diseases.objects.get(id=27))
# oncho =Images_or_Videos_of_disease(
#     link='https://pbs.twimg.com/media/DUODIX1X4AEL8sq.jpg',
#     disease=Diseases.objects.get(id=28))
# trypan =Images_or_Videos_of_disease(
#     link='https://www.cdc.gov/dpdx/trypanosomiasisafrican/modules/SleepingSick_LifeCycle_lg.jpg',
#     disease=Diseases.objects.get(id=29))
# dracun =Images_or_Videos_of_disease(
#     link='https://image.slidesharecdn.com/dracunculiasis-171219063653/95/dracunculiasis-control-programmeindia-13-638.jpg?cb=1513665642',
#     disease=Diseases.objects.get(id=30))
# echinoc =Images_or_Videos_of_disease(
#     link='https://www.cdc.gov/dpdx/echinococcosis/modules/Echinococcus_gran_LifeCycle_lg.jpg',
#     disease=Diseases.objects.get(id=31))
# japenc =Images_or_Videos_of_disease(
#     link='https://i1.wp.com/www.chiangraitimes.com/wp-content/uploads/2019/02/2d8753513fab9e126980dc9aa8858510.png?resize=740%2C740&ssl=1',
#     disease=Diseases.objects.get(id=32))
# forget3 =Images_or_Videos_of_disease(
#     link='https://img.huffingtonpost.com/asset/5dcc613f1f00009304dee539.jpeg?cache=QaTFuOj2IM&ops=crop_834_777_4651_2994%2Cscalefit_720_noupscale',
#     disease=Diseases.objects.get(id=33))
# avianflu =Images_or_Videos_of_disease(
#     link='https://1.bp.blogspot.com/-rDsPcuruxZk/WtXWvzZiDVI/AAAAAAAAqfI/jnBpxGbYlEgnveOEusW41h07uQ13nkvYQCLcBGAs/w1200-h630-p-k-no-nu/CDC%2BBird%2Bflu%2Bprevention.JPG',
#     disease=Diseases.objects.get(id=34))
# influenza =Images_or_Videos_of_disease(
#     link='https://www.nfid.org/wp-content/uploads/2019/08/Flu.jpg',
#     disease=Diseases.objects.get(id=35))
# cholera =Images_or_Videos_of_disease(
#     link='https://thumbs-prod.si-cdn.com/1WoaiAan_B_0mdcFxHv25ymlUSw=/420x240/https://public-media.si-cdn.com/filer/4b/f2/4bf2e8b7-75e0-42ff-b8d8-6fa3a83999cf/cholera.jpg',
#     disease=Diseases.objects.get(id=36))
# yaws =Images_or_Videos_of_disease(
#     link='https://www.msfaccess.org/sites/default/files/styles/msf_medium/public/2018-08/MSF125542%28High%29.jpg?itok=STdRx6d8',
#     disease=Diseases.objects.get(id=37))
# leprosy =Images_or_Videos_of_disease(
#     link='https://i.pinimg.com/originals/75/f3/df/75f3dfdecc5da08a3916b79abf466992.jpg',
#     disease=Diseases.objects.get(id=38))
# leish =Images_or_Videos_of_disease(
#     link='https://www.msdmanuals.com//-/media/manual/professional/images/leishmania_life_cycle_high.jpg?la=en&thn=0',
#     disease=Diseases.objects.get(id=39))
# diarr =Images_or_Videos_of_disease(
#     link='https://www.lenntech.com/images/diarrh1.jpg',
#     disease=Diseases.objects.get(id=40))
# taeniasis =Images_or_Videos_of_disease(
#     link='https://www.thelancet.com/cms/attachment/2000999980/2003718357/gr1.jpg',
#     disease=Diseases.objects.get(id=41))
# forget4 =Images_or_Videos_of_disease(
#     link='https://api.time.com/wp-content/uploads/2019/12/CatFilterReaction.jpg?w=600&quality=85',
#     disease=Diseases.objects.get(id=42))
# crimean =Images_or_Videos_of_disease(
#     link='https://thenativeantigencompany.com/wp-content/uploads/2019/04/shutterstock_1100550533.jpg',
#     disease=Diseases.objects.get(id=43))
# marburg =Images_or_Videos_of_disease(
#     link='https://upload.wikimedia.org/wikipedia/commons/9/99/Marburg_virus.jpg',
#     disease=Diseases.objects.get(id=44))
# monkey =Images_or_Videos_of_disease(
#     link='https://cdn.downtoearth.org.in/dte/userfiles/images/14-20150115.jpg',
#     disease=Diseases.objects.get(id=45))
# riftvall =Images_or_Videos_of_disease(
#     link='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1JqRTHzN8AnV7l4TkiE02b0MenpU7TaKMzAtxmBosvn6mZPHA&s',
#     disease=Diseases.objects.get(id=46))
# forget5 =Images_or_Videos_of_disease(
#     link='https://images.theconversation.com/files/301743/original/file-20191114-26207-lray93.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=926&fit=clip',
#     disease=Diseases.objects.get(id=47))
# lupus =Images_or_Videos_of_disease(
#     link='https://www.rheumatologynetwork.com/sites/default/files/%28%C2%A9Blueringmedia%2CAdobeStock%29.jpg',
#     disease=Diseases.objects.get(id=48))


# list_of_photos=[rabies, malaria, lassafever, tb, measles, meningcoccolmeningitus, chik, plague, aids, forget1,
#                 pneumia, rubella,poliomyelitis, hepb, buruliulcer, hepe, hepa, forget2, soiltrans, foodborntrem, ebola,
#                 hepc, yellowfever, dengue, trachoma, chagas, lymphaticfil, oncho, trypan, dracun, echinoc, japenc, forget3,
#                 avianflu, influenza, cholera, yaws, leprosy, leish, diarr, taeniasis, forget4, crimean, marburg, monkey, riftvall,
#                 forget5, lupus]
# for photo in list_of_photos:
#     photo.save()

# class Images_or_Videos_of_disease(models.Model):
#     link =models.CharField(max_length=1000) #??????????????????????? there is better
#     disease = models.ForeignKey('Diseases', on_delete=models.CASCADE)


# World_Diseases = Categories(name='World Diseases')
# Climate_Change = Categories(name='Climate Change')
# World_Hunger = Categories(name='World Hunger')

# list_of_problems =[World_Diseases, Climate_Change, World_Hunger]
# for problem in list_of_problems:
#     problem.save()

