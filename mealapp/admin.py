from django.contrib import admin
from .models import *

# Register your models here.
class ClothesAdmin(admin.ModelAdmin):
    list_display=('id', 'clothes_name','description' ,'size', 'color', 'brand_of_clothes','gender_of_clothes','publication', 'sent_at', 'update_at')
    list_display_links=('id', 'clothes_name')
    search_fields = ['clothes_name', 'description']
    list_editable = ('publication',)
    list_filter = ('publication', 'brand_of_clothes')
class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name', 'email', 'address', 'message', 'sent_at')

class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','name', 'last_name', 'number',  'address', 'message', 'sent_at')


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order)



admin.site.register(Contact,ContactAdmin)

admin.site.register(Brand)
admin.site.register(Gender_clothes)
admin.site.register(Clothes,ClothesAdmin)