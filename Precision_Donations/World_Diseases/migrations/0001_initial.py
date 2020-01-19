# Generated by Django 3.0.2 on 2020-01-07 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('offical_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('causes', models.CharField(max_length=5000, null=True)),
                ('diagnosis', models.CharField(max_length=5000, null=True)),
                ('symptoms', models.CharField(max_length=5000, null=True)),
                ('treatments', models.CharField(max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Research_labs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='World_Diseases.Countries')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='World_Diseases.Diseases')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rate_of_spread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('year', models.DateField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='World_Diseases.Diseases')),
            ],
        ),
        migrations.CreateModel(
            name='Images_or_Videos_of_disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='World_Diseases.Diseases')),
            ],
        ),
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_report', models.DateField()),
                ('amount_of_funding', models.FloatField()),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='World_Diseases.Research_labs')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='World_Diseases.Countries')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deaths_sufferers_per_country_per_year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deaths', models.IntegerField()),
                ('num_sufferers', models.IntegerField()),
                ('year', models.DateField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='World_Diseases.Countries')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='World_Diseases.Diseases')),
            ],
        ),
    ]
