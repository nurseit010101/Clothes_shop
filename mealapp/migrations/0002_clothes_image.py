# Generated by Django 4.1.2 on 2022-10-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Image'),
        ),
    ]
