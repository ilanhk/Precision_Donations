# Generated by Django 3.0.2 on 2020-01-07 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('World_Diseases', '0002_auto_20200107_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='research_labs',
            name='company_website',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
