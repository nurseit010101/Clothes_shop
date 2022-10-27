# Generated by Django 4.1.2 on 2022-10-26 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealapp', '0002_clothes_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('address', models.CharField(max_length=40, verbose_name='address')),
                ('message', models.CharField(max_length=80, verbose_name='message')),
                ('sent_at', models.DateTimeField(auto_now_add=True, verbose_name='Date and Time')),
            ],
        ),
    ]