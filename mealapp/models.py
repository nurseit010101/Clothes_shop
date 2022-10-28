from tabnanny import verbose
from django.db import models

# Create your models here.
class Brand(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Name of clothes')
    def __str__(self):
        return self.title
class Gender_clothes(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Gender of clothes')
    def __str__(self):
        return self.title


class Clothes(models.Model):
    clothes_name = models.CharField(max_length = 50, verbose_name = 'Name of clothes')
    description = models.TextField(verbose_name = 'Description', max_length = 200)
    image = models.ImageField(null = True, verbose_name = 'Image')
    size = models.IntegerField( verbose_name = 'Size of clothes')
    price = models.IntegerField( null = True, verbose_name = 'Price')
    color = models.CharField(max_length = 70,verbose_name = 'Color of clothes')
    brand_of_clothes = models.ForeignKey( Brand, on_delete = models.PROTECT, verbose_name = 'Brand of clothes')
    gender_of_clothes = models.ForeignKey( Gender_clothes, on_delete = models.PROTECT, verbose_name = 'Gender of clothes')
    publication = models.BooleanField(verbose_name = 'Publication', default = True)
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Date and Time')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Update Time')

class SneakerCard(models.Model):
    tittle = models.CharField(max_length = 50, verbose_name = 'Название')
    description = models.TextField(verbose_name = 'Описание')
    price = models.IntegerField(verbose_name = 'Цена')
    image = models.ImageField(upload_to = 'mainapp', verbose_name = 'Изображение' )

    Category = models.ForeignKey(Brand,
    verbose_name = 'Бренд', on_delete = models.CASCADE)

class Contact(models.Model):
    name = models.CharField(max_length=40, verbose_name='name')
    email = models.EmailField(verbose_name='email')
    address = models.CharField(max_length=40, verbose_name='address')
    message = models.CharField(max_length=80, verbose_name='message')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Date and Time')

class Customer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    message = models.TextField(verbose_name='Message')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Date and Time')


class Order(models.Model):
    product = models.CharField(max_length=500, verbose_name='Order')
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, verbose_name='Client')
    total_price = models.IntegerField(verbose_name='Total price')
    phone = models.IntegerField(verbose_name='Phone number')
    address = models.CharField(max_length=500, null=True, verbose_name='Addres')
    sent_at = models.DateField(auto_now_add=True, verbose_name='Date')