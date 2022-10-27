from .models import Clothes
from mealapp.models import *
from .serializers import ClothesSerializer
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .api import *
from collections import Counter
# Create your views here.

Clothes
class ClothesAPIList(generics.ListCreateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

class ClothesAPIUpdate(generics.UpdateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

class ClothesAPIDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer



def index(request):
    return render(request, 'index1.html' ,{'zipped_lst':zipped_lst})
def catalog(request):
    return render(request, 'catalog.html')
def contackts(request):
    return render(request, 'contackts.html')


def message(request):
    if request.method=='POST':
        send=Contact()
        send.name=request.POST.get('name')
        send.email=request.POST.get('email')
        send.address=request.POST.get('address')
        send.message=request.POST.get('message')
        send.save()
        return HttpResponseRedirect('/')


def signUp(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST  )
        if user.is_valid():
            user.save()
            return HttpResponseRedirect('/')

    else:
        user = UserCreationForm()
    return render(request, 'signup.html', {'user':user})
def signin(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request , username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

        else:
            form = AuthenticationForm()
        return render(request, 'auth.html', {'user':form})
    except UnboundLocalError:
        return render(request, 'error.html')

def signout(request):
    logout(request)
    return HttpResponseRedirect('/')

def addCart(request, id):
    cart_session = request.session.get('cart_session', [])
    cart_session.append(id)
    request.session['cart_session'] = cart_session
    return HttpResponseRedirect('/')

def cart(request):
    cart_session = request.session.get('cart_session', [])
    count_of_product = len(cart_session)
    products_cart =[]
    all_products_sum = 0
    for j in cart_session:
        for i in zipped_lst:
            if i[0] == j:
                products_cart.append(i)
                all_products_sum+=i[4]
    
    product = Counter(products_cart)
    lst = []
    for p, c in product.items():
        lst.append([p,c])
    return render(request, 'cart.html',{'count_of_product': count_of_product, 'all_products_sum': all_products_sum , 'lst':lst} )


def removeCart(request ,id):
    try:
        cart_session = request.session.get('cart_session', [])
        carts = []
        carts = cart_session
        carts.remove(id)
        request.session['cart_session'] = carts
        return HttpResponseRedirect('/cart')
    except:
        return HttpResponseRedirect('/cart')
